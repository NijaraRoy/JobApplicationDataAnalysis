from src.utils import *

class JobApplication:
    """
    This is Base class representing a job application.
    """

    def __init__(self, date, title, company, job_type, experience, salary, interview_difficulty):
        """
        Initializes a JobApplication object.

        Args:
            date (str): The application date.
            title (str): Job title.
            company (str): Company providing the job.
            job_type (str): Type of job (Stem/non-Stem).
            experience (int): Years of experience needed.
            salary (float): Salary in USD.
            interview_difficulty (float): Difficulty rating.
        """
        self.date = date
        self.title = title
        self.company = company
        self.type = job_type
        self.experience = experience
        self.salary = salary
        self.interview_difficulty = interview_difficulty
        self.unique_id = id(self)

    def __str__(self):
        """
        Returns a formatted string representation of the JobApplication object.

        Returns:
            str: Comma-separated string of all attributes.
        """
        return f"{self.unique_id},{self.date},{self.title},{self.company},{self.type},{self.experience},{self.salary},{self.interview_difficulty}"
    


class StemJobApplication(JobApplication):
    """
    Subclass of JobApplication representing a STEM job.
    """
    def __init__(self, date, title, company, experience, salary, interview_difficulty):
        """
        Initializes a StemJobApplication object.

        Args:
            date (str): The application date.
            title (str): Job title.
            company (str): Company providing the job.
            experience (int): Years of experience needed.
            salary (float): Salary in USD.
            interview_difficulty (float): Difficulty rating.
        """
        super().__init__(date, title, company, "Stem", experience, salary, interview_difficulty)



class NonStemJobApplication(JobApplication):
    """
    Subclass of JobApplication representing a non-STEM job.
    """
    def __init__(self, date, title, company, experience, salary, interview_difficulty):
        """
        Initializes a NonStemJobApplication object.

        Args:
            date (str): The application date.
            title (str): Job title.
            company (str): Company providing the job.
            experience (int): Years of experience needed.
            salary (float): Salary in USD.
            interview_difficulty (float): Difficulty rating.
        """
        super().__init__(date, title, company, "non-Stem", experience, salary, interview_difficulty)


class Apple(StemJobApplication):
    """
    Subclass of StemJobApplication representing an Apple job.
    """
    def __init__(self, date, title, experience, salary, interview_difficulty):
        """
        Initializes an Apple job application.

        Args:
            date (str): The application date.
            title (str): Job title.
            experience (int): Years of experience needed.
            salary (float): Salary in USD.
            interview_difficulty (float): Difficulty rating.
        """
        super().__init__(date, title, "Apple", experience, salary, interview_difficulty)


class Siemens(NonStemJobApplication):
    """
    Subclass of NonStemJobApplication representing a Siemens job.
    """
    def __init__(self, date, title, experience, salary, interview_difficulty):
        """
        Initializes a Siemens job application.

        Args:
            date (str): The application date.
            title (str): Job title.
            experience (int): Years of experience needed.
            salary (float): Salary in USD.
            interview_difficulty (float): Difficulty rating.
        """
        super().__init__(date, title, "Siemens", experience, salary, interview_difficulty)


class Boeing(NonStemJobApplication):
    """
    Subclass of NonStemJobApplication representing a Boeing job.
    """
    def __init__(self, date, title, experience, salary, interview_difficulty):
        """
        Initializes a Boeing job application.

        Args:
            date (str): The application date.
            title (str): Job title.
            experience (int): Years of experience needed.
            salary (float): Salary in USD.
            interview_difficulty (float): Difficulty rating.
        """
        super().__init__(date, title, "Boeing", experience, salary, interview_difficulty)
