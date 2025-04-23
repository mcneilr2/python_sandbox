
# Entrypoint for a Python script inside Docker
import os

def main():
    job_name = os.getenv("JOB_NAME", "default_job")
    print(f"Running job: {job_name}")

if __name__ == "__main__":
    main()
