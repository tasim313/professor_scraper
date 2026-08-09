from rest_framework import serializers
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

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class SourceSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceSnapshot
        fields = '__all__'

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'

class UniversityAliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityAlias
        fields = '__all__'

class LivingCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivingCost
        fields = '__all__'

class AdmissionRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionRequirement
        fields = '__all__'

class LanguageRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageRequirement
        fields = '__all__'

class ApplicationDeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDeadline
        fields = '__all__'

class FundingOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingOpportunity
        fields = '__all__'

class FundingSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingSubject
        fields = '__all__'

class FundingEligibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FundingEligibility
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'

class AdPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdPlacement
        fields = '__all__'

class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = '__all__'

class ScholarshipCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipCountry
        fields = '__all__'

class ScholarshipDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipDegree
        fields = '__all__'

class ScholarshipSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipSubject
        fields = '__all__'

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

class NewsletterCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterCampaign
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class TuitionFeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuitionFee
        fields = '__all__'

class PageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageView
        fields = '__all__'

class ScraperSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScraperSource
        fields = '__all__'

class ScraperJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScraperJob
        fields = '__all__'

class ScraperResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScraperResult
        fields = '__all__'

class DataChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataChange
        fields = '__all__'

class VerificationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationRecord
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class ProfessorSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorSubject
        fields = '__all__'

class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = '__all__'

class AccreditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accreditation
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class SubjectAliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectAlias
        fields = '__all__'

class ResearchGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchGroup
        fields = '__all__'

class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'

class ResearchProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchProject
        fields = '__all__'

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class ProgramSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramSubject
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'

class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = '__all__'

class SearchQueryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchQueryLog
        fields = '__all__'

