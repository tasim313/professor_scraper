from rest_framework import viewsets
from . import serializers
from apps.sources.models import Source
from apps.sources.models import SourceSnapshot
from apps.universities.models import University
from apps.universities.models import Campus
from apps.universities.models import UniversityAlias
from apps.living_cost.models import LivingCost
from apps.admissions.models import AdmissionRequirement
from apps.admissions.models import LanguageRequirement
from apps.admissions.models import ApplicationDeadline
from apps.funding.models import FundingOpportunity
from apps.funding.models import FundingSubject
from apps.funding.models import FundingEligibility
from apps.countries.models import Country
from apps.countries.models import City
from apps.advertising.models import Sponsor
from apps.advertising.models import AdPlacement
from apps.scholarships.models import Scholarship
from apps.scholarships.models import ScholarshipCountry
from apps.scholarships.models import ScholarshipDegree
from apps.scholarships.models import ScholarshipSubject
from apps.newsletters.models import Subscriber
from apps.newsletters.models import NewsletterCampaign
from apps.departments.models import Faculty
from apps.departments.models import Department
from apps.tuition.models import TuitionFee
from apps.analytics.models import PageView
from apps.scraping.models import ScraperSource
from apps.scraping.models import ScraperJob
from apps.scraping.models import ScraperResult
from apps.verification.models import DataChange
from apps.verification.models import VerificationRecord
from apps.professors.models import Professor
from apps.professors.models import ProfessorSubject
from apps.rankings.models import Ranking
from apps.rankings.models import Accreditation
from apps.subjects.models import Subject
from apps.subjects.models import SubjectAlias
from apps.research.models import ResearchGroup
from apps.research.models import Laboratory
from apps.research.models import ResearchProject
from apps.degrees.models import Degree
from apps.programs.models import Program
from apps.programs.models import ProgramSubject
from apps.notifications.models import Notification
from apps.subscriptions.models import SubscriptionPlan
from apps.subscriptions.models import UserSubscription
from apps.search.models import SearchQueryLog

class SourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Source.objects.all()
    serializer_class = serializers.SourceSerializer

class SourceSnapshotViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SourceSnapshot.objects.all()
    serializer_class = serializers.SourceSnapshotSerializer

class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = University.objects.all()
    serializer_class = serializers.UniversitySerializer

class CampusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = serializers.CampusSerializer

class UniversityAliasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UniversityAlias.objects.all()
    serializer_class = serializers.UniversityAliasSerializer

class LivingCostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LivingCost.objects.all()
    serializer_class = serializers.LivingCostSerializer

class AdmissionRequirementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdmissionRequirement.objects.all()
    serializer_class = serializers.AdmissionRequirementSerializer

class LanguageRequirementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LanguageRequirement.objects.all()
    serializer_class = serializers.LanguageRequirementSerializer

class ApplicationDeadlineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApplicationDeadline.objects.all()
    serializer_class = serializers.ApplicationDeadlineSerializer

class FundingOpportunityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FundingOpportunity.objects.all()
    serializer_class = serializers.FundingOpportunitySerializer

class FundingSubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FundingSubject.objects.all()
    serializer_class = serializers.FundingSubjectSerializer

class FundingEligibilityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FundingEligibility.objects.all()
    serializer_class = serializers.FundingEligibilitySerializer

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = serializers.CountrySerializer

class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = serializers.CitySerializer

class SponsorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = serializers.SponsorSerializer

class AdPlacementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdPlacement.objects.all()
    serializer_class = serializers.AdPlacementSerializer

class ScholarshipViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Scholarship.objects.all()
    serializer_class = serializers.ScholarshipSerializer

class ScholarshipCountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScholarshipCountry.objects.all()
    serializer_class = serializers.ScholarshipCountrySerializer

class ScholarshipDegreeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScholarshipDegree.objects.all()
    serializer_class = serializers.ScholarshipDegreeSerializer

class ScholarshipSubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScholarshipSubject.objects.all()
    serializer_class = serializers.ScholarshipSubjectSerializer

class SubscriberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = serializers.SubscriberSerializer

class NewsletterCampaignViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsletterCampaign.objects.all()
    serializer_class = serializers.NewsletterCampaignSerializer

class FacultyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = serializers.FacultySerializer

class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

class TuitionFeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TuitionFee.objects.all()
    serializer_class = serializers.TuitionFeeSerializer

class PageViewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PageView.objects.all()
    serializer_class = serializers.PageViewSerializer

class ScraperSourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScraperSource.objects.all()
    serializer_class = serializers.ScraperSourceSerializer

class ScraperJobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScraperJob.objects.all()
    serializer_class = serializers.ScraperJobSerializer

class ScraperResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ScraperResult.objects.all()
    serializer_class = serializers.ScraperResultSerializer

class DataChangeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DataChange.objects.all()
    serializer_class = serializers.DataChangeSerializer

class VerificationRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VerificationRecord.objects.all()
    serializer_class = serializers.VerificationRecordSerializer

class ProfessorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = serializers.ProfessorSerializer

class ProfessorSubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProfessorSubject.objects.all()
    serializer_class = serializers.ProfessorSubjectSerializer

class RankingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = serializers.RankingSerializer

class AccreditationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Accreditation.objects.all()
    serializer_class = serializers.AccreditationSerializer

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = serializers.SubjectSerializer

class SubjectAliasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubjectAlias.objects.all()
    serializer_class = serializers.SubjectAliasSerializer

class ResearchGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ResearchGroup.objects.all()
    serializer_class = serializers.ResearchGroupSerializer

class LaboratoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Laboratory.objects.all()
    serializer_class = serializers.LaboratorySerializer

class ResearchProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ResearchProject.objects.all()
    serializer_class = serializers.ResearchProjectSerializer

class DegreeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = serializers.DegreeSerializer

class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Program.objects.all()
    serializer_class = serializers.ProgramSerializer

class ProgramSubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProgramSubject.objects.all()
    serializer_class = serializers.ProgramSubjectSerializer

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = serializers.NotificationSerializer

class SubscriptionPlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = serializers.SubscriptionPlanSerializer

class UserSubscriptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = serializers.UserSubscriptionSerializer

class SearchQueryLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SearchQueryLog.objects.all()
    serializer_class = serializers.SearchQueryLogSerializer

