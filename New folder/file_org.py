import os

def main():

    main_directory = "MyFiles"

    try:

        os.mkdir(main_directory)
        print(f"Directory '{main_directory}' created successfully.")


        subdirectories = ["Docs", "Images", "Videos"]


        for subdir in subdirectories:
            subdir_path = os.path.join(main_directory, subdir)
            os.mkdir(subdir_path)
            print(f"Subdirectory '{subdir}' created successfully.")

    except FileExistsError:
        print(f"Directory '{main_directory}' already exists.")


main()