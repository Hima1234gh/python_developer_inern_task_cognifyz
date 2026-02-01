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

# Automated File Organizer
class FileOrganizer:
    def __init__(self, source_dir, dest_dir, dry_run=False, ignore_extensions=None):
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.dry_run = dry_run
        self.ignore_extensions = ignore_extensions or []
        # Setup logging
        logging.basicConfig(
            filename="organizer.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
    # Helper method to get a unique filename
    def _get_unique_filename(self, directory, filename):
        base, ext = os.path.splitext(filename)
        counter = 1
        new_filename = filename

        while os.path.exists(os.path.join(directory, new_filename)):
            new_filename = f"{base}_{counter}{ext}"
            counter += 1

        return new_filename
    # Organize files by type
    def organize_by_type(self):
        for filename in os.listdir(self.source_dir):
            file_path = os.path.join(self.source_dir, filename)

            if not os.path.isfile(file_path):
                continue

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
    # Organize files by modification date
    def organize_by_date(self):
        for filename in os.listdir(self.source_dir):
            file_path = os.path.join(self.source_dir, filename)

            if not os.path.isfile(file_path):
                continue

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

