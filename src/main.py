import sys
sys.path.append('./')
import os

from src.utils import *
from src.job_application_data_constructor import *

def main():
    # get all input variables
    project_variables = load_yaml('project_variables.yaml')
    job_details = project_variables['job_details']
  
    # # Build and test OOP classes given in the instruction set
    # # Create instances of all classes
    job_application = JobApplication(*tuple(job_details['generic_job_details']))
    stem_job_application = StemJobApplication(*tuple(job_details['stem_job_details']))
    non_stem_job_application = NonStemJobApplication(*tuple(job_details['nonstem_job_details']))
    apple_job_application = Apple(*tuple(job_details['apple_job_details']))
    siemens_job_application = Siemens(*tuple(job_details['siemens_job_details']))
    boeing_job_application = Boeing(*tuple(job_details['boeing_job_details']))

    # Print the string representation of each object
    print("JobApplication:", str(job_application))
    print("StemJobApplication:", str(stem_job_application))
    print("NonStemJobApplication:", str(non_stem_job_application))
    print("AppleJobApplication:", str(apple_job_application))
    print("SiemensJobApplication:", str(siemens_job_application))
    print("BoeingJobApplication:", str(boeing_job_application))

    # Save all objects to a CSV file
    all_objects = [
        job_application,
        stem_job_application,
        non_stem_job_application,
        apple_job_application,
        siemens_job_application,
        boeing_job_application
    ]
    
    save_to_csv(all_objects, project_variables['output_csv_loc'])


if __name__ == "__main__":
    main()

