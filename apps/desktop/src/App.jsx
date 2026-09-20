import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import { ThemeProvider } from './contexts/ThemeContext';
import { DomainProvider } from './contexts/DomainContext';
import AppLayout from './components/layout/AppLayout';
import TopicSelectionModal from './components/common/TopicSelectionModal';
import Dashboard from './pages/Dashboard';
import Courses from './pages/Courses';
import CourseDetail from './pages/CourseDetail';
import LessonPage from './pages/LessonPage';
import SkillTreePage from './pages/SkillTreePage';
import SettingsPage from './pages/SettingsPage';
import AlgorithmLabPage from './pages/AlgorithmLabPage';
import DeepLearningLabPage from './pages/DeepLearningLabPage';
import BreakTheModelPage from './pages/BreakTheModelPage';
import WebDevLabPage from './pages/WebDevLabPage';
import MobileAppLabPage from './pages/MobileAppLabPage';
import SystemDesignLabPage from './pages/SystemDesignLabPage';
import GitLabPage from './pages/GitLabPage';
import PlaygroundPage from './pages/PlaygroundPage';
import ChallengesPage from './pages/ChallengesPage';
import ChallengeDetailPage from './pages/ChallengeDetailPage';
import DatasetsPage from './pages/DatasetsPage';
import ExperimentsPage from './pages/ExperimentsPage';
import TutorPage from './pages/TutorPage';
import ProjectsPage from './pages/ProjectsPage';
import ProjectDetailPage from './pages/ProjectDetailPage';
import AchievementsPage from './pages/AchievementsPage';
import ResearchPage from './pages/ResearchPage';
import PaperDetailPage from './pages/PaperDetailPage';
import InterviewsPage from './pages/InterviewsPage';
import InterviewSessionPage from './pages/InterviewSessionPage';
import HackathonsPage from './pages/HackathonsPage';
import CommunityPage from './pages/CommunityPage';
import CareerPage from './pages/CareerPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import FeatureTeaserPage from './pages/FeatureTeaserPage';
import LoadingSpinner from './components/common/LoadingSpinner';

function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();
  if (loading) return <LoadingSpinner message="Authenticating session..." />;
  if (!user) return <Navigate to="/login" replace />;
  return children;
}

export default function App() {
  return (
    <ThemeProvider>
      <AuthProvider>
        <DomainProvider>
          <BrowserRouter future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
            <TopicSelectionModal />
            <Routes>
              {/* Public Auth Routes */}
              <Route path="/login" element={<LoginPage />} />
              <Route path="/register" element={<RegisterPage />} />

              {/* Authenticated Desktop Shell */}
              <Route
                path="/"
                element={
                  <ProtectedRoute>
                    <AppLayout />
                  </ProtectedRoute>
                }
              >
                <Route index element={<Navigate to="/dashboard" replace />} />
                <Route path="dashboard" element={<Dashboard />} />
                <Route path="learn" element={<Courses />} />
                <Route path="courses/:courseSlug" element={<CourseDetail />} />
                <Route path="lessons/:lessonSlug" element={<LessonPage />} />
                <Route path="skills" element={<SkillTreePage />} />
                
                {/* Domain Specialized Labs */}
                <Route path="algorithms" element={<AlgorithmLabPage />} />
                <Route path="deep-learning" element={<DeepLearningLabPage />} />
                <Route path="break-the-model" element={<BreakTheModelPage />} />
                <Route path="web-lab" element={<WebDevLabPage />} />
                <Route path="app-lab" element={<MobileAppLabPage />} />
                <Route path="system-design-lab" element={<SystemDesignLabPage />} />
                <Route path="git-lab" element={<GitLabPage />} />
                
                <Route path="playground" element={<PlaygroundPage />} />
                <Route path="challenges" element={<ChallengesPage />} />
                <Route path="challenges/:challengeId" element={<ChallengeDetailPage />} />
                <Route path="settings" element={<SettingsPage />} />

                <Route path="datasets" element={<DatasetsPage />} />
                <Route path="experiments" element={<ExperimentsPage />} />
                <Route path="tutor" element={<TutorPage />} />
                <Route path="projects" element={<ProjectsPage />} />
                <Route path="projects/:projectId" element={<ProjectDetailPage />} />
                <Route path="research" element={<ResearchPage />} />
                <Route path="research/:paperId" element={<PaperDetailPage />} />
                <Route path="interviews" element={<InterviewsPage />} />
                <Route path="interviews/:trackId" element={<InterviewSessionPage />} />
                <Route path="hackathons" element={<HackathonsPage />} />
                <Route path="community" element={<CommunityPage />} />
                <Route path="career" element={<CareerPage />} />
                <Route path="achievements" element={<AchievementsPage />} />
              </Route>

              {/* Fallback */}
              <Route path="*" element={<Navigate to="/dashboard" replace />} />
            </Routes>
          </BrowserRouter>
        </DomainProvider>
      </AuthProvider>
    </ThemeProvider>
  );
}
