from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.schemas.dataset import (
    DatasetListItem,
    DatasetProfileResponse,
    CustomDatasetUploadRequest
)
from app.services.dataset_service import (
    list_all_datasets,
    load_dataset_dataframe,
    profile_dataframe,
    register_custom_csv_dataset
)

router = APIRouter(prefix="/datasets", tags=["Datasets"])

@router.get("", response_model=List[DatasetListItem])
async def get_datasets():
    """Retrieve catalog of built-in benchmark datasets and custom uploads."""
    return list_all_datasets()

@router.get("/{dataset_id}", response_model=DatasetProfileResponse)
async def get_dataset_profile(dataset_id: str):
    """Retrieve in-depth exploratory profile, correlation matrix, and data quality warnings for a dataset."""
    try:
        df, name, desc, task_type, target_col = load_dataset_dataframe(dataset_id)
        return profile_dataframe(dataset_id, df, name, desc, task_type, target_col)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to profile dataset: {str(e)}")

@router.post("/upload", response_model=DatasetProfileResponse)
async def upload_custom_dataset(req: CustomDatasetUploadRequest):
    """Upload and dynamically profile a custom CSV dataset."""
    try:
        return register_custom_csv_dataset(
            name=req.name,
            description=req.description,
            task_type=req.task_type,
            target_column=req.target_column,
            csv_content=req.csv_content
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to process uploaded CSV: {str(e)}")
