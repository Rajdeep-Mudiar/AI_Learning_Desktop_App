import math
from typing import List
from app.schemas.simulation import (
    Point2D, RegressionStepRequest, RegressionStepResponse,
    KMeansStepRequest, KMeansStepResponse, PCARequest, PCAResponse
)

class SimulationService:
    @staticmethod
    def step_linear_regression(req: RegressionStepRequest) -> RegressionStepResponse:
        N = max(1, len(req.points))
        residuals = []
        sum_err_x = 0.0
        sum_err = 0.0
        total_sq_err = 0.0

        for pt in req.points:
            y_pred = req.weight * pt.x + req.bias
            err = y_pred - pt.y
            residuals.append(round(err, 4))
            sum_err_x += err * pt.x
            sum_err += err
            total_sq_err += err ** 2

        mse = total_sq_err / N
        grad_w = (2.0 / N) * sum_err_x
        grad_b = (2.0 / N) * sum_err

        new_w = req.weight - req.learning_rate * grad_w
        new_b = req.bias - req.learning_rate * grad_b

        return RegressionStepResponse(
            new_weight=round(new_w, 4),
            new_bias=round(new_b, 4),
            mse_loss=round(mse, 4),
            gradient_w=round(grad_w, 4),
            gradient_b=round(grad_b, 4),
            residuals=residuals
        )

    @staticmethod
    def step_kmeans(req: KMeansStepRequest) -> KMeansStepResponse:
        if not req.centroids or not req.points:
            return KMeansStepResponse(assignments=[], new_centroids=req.centroids, inertia=0.0, converged=True)

        k = len(req.centroids)
        assignments = []
        inertia = 0.0

        # Phase 1: Assign to nearest centroid
        for pt in req.points:
            best_c = 0
            min_dist_sq = float('inf')
            for c_idx, c in enumerate(req.centroids):
                dist_sq = (pt.x - c.x) ** 2 + (pt.y - c.y) ** 2
                if dist_sq < min_dist_sq:
                    min_dist_sq = dist_sq
                    best_c = c_idx
            assignments.append(best_c)
            inertia += min_dist_sq

        # Phase 2: Compute new centroid centers
        new_centroids = []
        converged = True
        for c_idx in range(k):
            cluster_pts = [req.points[i] for i, a in enumerate(assignments) if a == c_idx]
            if cluster_pts:
                avg_x = sum(p.x for p in cluster_pts) / len(cluster_pts)
                avg_y = sum(p.y for p in cluster_pts) / len(cluster_pts)
            else:
                avg_x = req.centroids[c_idx].x
                avg_y = req.centroids[c_idx].y

            old_c = req.centroids[c_idx]
            if math.hypot(avg_x - old_c.x, avg_y - old_c.y) > 0.001:
                converged = False

            new_centroids.append(Point2D(x=round(avg_x, 3), y=round(avg_y, 3)))

        return KMeansStepResponse(
            assignments=assignments,
            new_centroids=new_centroids,
            inertia=round(inertia, 3),
            converged=converged
        )

    @staticmethod
    def compute_pca(req: PCARequest) -> PCAResponse:
        pts = req.points
        N = len(pts)
        if N < 2:
            return PCAResponse(
                mean=Point2D(x=0, y=0),
                components=[Point2D(x=1, y=0), Point2D(x=0, y=1)],
                eigenvalues=[1.0, 0.0],
                explained_variance_ratio=[1.0, 0.0],
                projected_points=pts
            )

        # 1. Mean center
        mean_x = sum(p.x for p in pts) / N
        mean_y = sum(p.y for p in pts) / N

        centered_x = [p.x - mean_x for p in pts]
        centered_y = [p.y - mean_y for p in pts]

        # 2. Covariance matrix 2x2
        cov_xx = sum(cx * cx for cx in centered_x) / (N - 1)
        cov_xy = sum(cx * cy for cx, cy in zip(centered_x, centered_y)) / (N - 1)
        cov_yy = sum(cy * cy for cy in centered_y) / (N - 1)

        # 3. Eigenvalues of 2x2 symmetric matrix
        # Trace and Determinant
        trace = cov_xx + cov_yy
        det = cov_xx * cov_yy - cov_xy * cov_xy
        discriminant = max(0.0, (trace / 2.0) ** 2 - det)
        sqrt_disc = math.sqrt(discriminant)

        lambda1 = (trace / 2.0) + sqrt_disc
        lambda2 = max(0.0, (trace / 2.0) - sqrt_disc)

        # Eigenvector 1 for lambda1
        if abs(cov_xy) > 1e-7:
            v1_x = lambda1 - cov_yy
            v1_y = cov_xy
        elif cov_xx >= cov_yy:
            v1_x, v1_y = 1.0, 0.0
        else:
            v1_x, v1_y = 0.0, 1.0

        norm1 = math.hypot(v1_x, v1_y)
        if norm1 > 0:
            v1_x /= norm1
            v1_y /= norm1

        # Eigenvector 2 is perpendicular to v1
        v2_x, v2_y = -v1_y, v1_x

        total_var = max(1e-9, lambda1 + lambda2)
        ratio1 = round(lambda1 / total_var, 3)
        ratio2 = round(lambda2 / total_var, 3)

        # Project points onto PC1
        projected = []
        for cx, cy in zip(centered_x, centered_y):
            # scalar projection along v1
            proj_val = cx * v1_x + cy * v1_y
            projected.append(Point2D(
                x=round(mean_x + proj_val * v1_x, 3),
                y=round(mean_y + proj_val * v1_y, 3)
            ))

        return PCAResponse(
            mean=Point2D(x=round(mean_x, 3), y=round(mean_y, 3)),
            components=[
                Point2D(x=round(v1_x, 4), y=round(v1_y, 4)),
                Point2D(x=round(v2_x, 4), y=round(v2_y, 4))
            ],
            eigenvalues=[round(lambda1, 3), round(lambda2, 3)],
            explained_variance_ratio=[ratio1, ratio2],
            projected_points=projected
        )
