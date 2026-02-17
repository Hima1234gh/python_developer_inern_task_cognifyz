"""Identify a repetitive task, such as data
processing, file management, or report
generation, and develop a script to
automate it using Python. This task will
showcase their problem-solving skills and
familiarity with Python's automation
capabilities."""


import os
import shutil
import logging
import argparse
from datetime import datetime
from dataclasses import dataclass

# Automated File Organizer
@dataclass
class FileOrganizer:
    source_dir: str
    dest_dir: str   
    dry_run: bool = False
    def __init__(self,ignore_extensions=None):
        
        self.ignore_extensions = ignore_extensions or []

        logging.basicConfig(
            filename="organizer.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def _get_unique_filename(self, directory, filename):
        base, ext = os.path.splitext(filename)
        counter = 1
        new_filename = filename

        try:
            while os.path.exists(os.path.join(directory, new_filename)):
                new_filename = f"{base}_{counter}{ext}"
                counter += 1
        except OSError as e:
            logging.error(f"Error checking filename uniqueness: {e}")

        return new_filename

    def organize_by_type(self):
        try:
            files = os.listdir(self.source_dir)
        except FileNotFoundError:
            logging.error("Source directory not found.")
            print("Error: Source directory not found.")
            return
        except PermissionError:
            logging.error("Permission denied while accessing source directory.")
            print("Error: Permission denied.")
            return

        for filename in files:
            file_path = os.path.join(self.source_dir, filename)

            if not os.path.isfile(file_path):
                continue

            try:
                extension = os.path.splitext(filename)[1][1:].lower() or "no_extension"

                if extension in self.ignore_extensions:
                    continue

                target_dir = os.path.join(self.dest_dir, extension)
                os.makedirs(target_dir, exist_ok=True)

                new_name = self._get_unique_filename(target_dir, filename)
                destination = os.path.join(target_dir, new_name)

                if self.dry_run:
                    print(f"[DRY RUN] {filename} → {target_dir}")
                else:
                    shutil.move(file_path, destination)
                    logging.info(f"Moved {filename} → {destination}")

            except Exception as e:
                logging.error(f"Failed to move file {filename}: {e}")

    def organize_by_date(self):
        try:
            files = os.listdir(self.source_dir)
        except FileNotFoundError:
            logging.error("Source directory not found.")
            print("Error: Source directory not found.")
            return
        except PermissionError:
            logging.error("Permission denied while accessing source directory.")
            print("Error: Permission denied.")
            return

        for filename in files:
            file_path = os.path.join(self.source_dir, filename)

            if not os.path.isfile(file_path):
                continue

            try:
                mod_time = os.path.getmtime(file_path)
                mod_date = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")

                target_dir = os.path.join(self.dest_dir, mod_date)
                os.makedirs(target_dir, exist_ok=True)

                new_name = self._get_unique_filename(target_dir, filename)
                destination = os.path.join(target_dir, new_name)

                if self.dry_run:
                    print(f"[DRY RUN] {filename} → {target_dir}")
                else:
                    shutil.move(file_path, destination)
                    logging.info(f"Moved {filename} → {destination}")

            except Exception as e:
                logging.error(f"Failed to process file {filename}: {e}")


# Command-Line Interface
class OrganizerCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="Automated File Organizer (CLI Tool)"
        )
        self._setup_arguments()
    # Setup command-line arguments
    def _setup_arguments(self):
        self.parser.add_argument("source", help="Source directory")
        self.parser.add_argument("destination", help="Destination directory")

        self.parser.add_argument(
            "--mode",
            choices=["type", "date"],
            required=True,
            help="Organize files by type or modification date"
        )

        self.parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Simulate actions without moving files"
        )

        self.parser.add_argument(
            "--ignore",
            nargs="*",
            default=[],
            help="File extensions to ignore (e.g. tmp log)"
        )
    # Run the CLI
    def run(self):
        args = self.parser.parse_args()

        organizer = FileOrganizer(
            source_dir=args.source,
            dest_dir=args.destination,
            dry_run=args.dry_run,
            ignore_extensions=args.ignore
        )

        if args.mode == "type":
            organizer.organize_by_type()
        else:
            organizer.organize_by_date()

# Main execution
if __name__ == "__main__":
    cli = OrganizerCLI()
    cli.run()

# Exectution trial

# python3 Level_3/Task_3.py  ~/target  ~/destination  --mode date  
# To sort the files by dates

# python3 Level_3/Task_3.py  ~/target ~/destination  --mode type
# To sort the files by types