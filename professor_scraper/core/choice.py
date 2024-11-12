from django.db import models

class UserRole(models.TextChoices):
    STUDENT = 'student', 'Student' # Represents students who will be the primary audience for accessing information  about professors, research opportunities, and scholarships.
    TEACHER = 'teacher', 'Teacher' # Represents teachers who may be involved in education but are distinct from professors and may require different permissions or views.
    UNIVERSITY = 'university', 'University' # Universities or educational institutions; this role could be used for institution-wide accounts  that manage multiple professors or submit general scholarship opportunities.
    PROFESSOR  = 'professor', 'Professor' # Professors who are the focus of the platform; they may update their profiles, share research, and interact with students and other users.
    ORGANIZATION = 'organization' 'Organization' # Organizations, such as research institutes or foundations, that want to connect with students or offer scholarships. This is useful for larger institutions that aren't universities.
    # Researchers or research assistants who might not have a teaching role but want to share 
    # their research or connect with other researchers and students.
    RESEARCHER = 'researcher', 'Researcher'  # For independent researchers or research assistants
    # Accounts for organizations or individuals specifically providing scholarships. This role 
    # could help them manage scholarship listings and applications.
    SCHOLARSHIP_PROVIDER = 'scholarship_provider', 'Scholarship Provider'  # Organizations providing scholarships
    # Former students who may wish to connect with professors or explore ongoing research 
    # and networking opportunities.
    ALUMNI = 'alumni', 'Alumni'  # Former students who may want to stay connected
    # Moderators who are responsible for monitoring and moderating content, such as comments or 
    # discussions on the platform, to maintain a safe and respectful environment.
    MODERATOR = 'moderator', 'Moderator'  # Users who help moderate content or discussions
    VISITOR = 'visitor', 'Visitor'  # Unregistered users who can browse public information
    ADMIN = 'admin', 'Admin' # Administrative role with the highest level of access, capable of managing users, content, and system settings across the platform.
    SUPPORT = 'support', 'Customer Support' # Customer support role to assist users with technical issues or answer questions about using the platform. This role may be limited to help desk functions.



class UserStatus(models.TextChoices):
    # Represents an active user account, indicating that the user is currently able to access the platform.
    Active = 'Active', 'active'
    # Represents an inactive user account, indicating that the user cannot currently access the platform.
    Inactive = 'Inactive', 'inactive'



class Gender(models.TextChoices):
    # Represents female gender option for user profiles.
    FEMALE = "female", "Female"
    # Represents male gender option for user profiles.
    MALE = "male", "Male"
    # Represents non-binary, other, or undisclosed gender identities.
    OTHERS = "others", "Others"