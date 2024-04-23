def main():
   
    try:
       
        date_time = input("Enter the current date and time (e.g., April 23, 2024 10:00 AM): ")
        

        entry = input("Enter your diary entry: ")

      
        with open('diary.txt', 'a') as file:
        
            file.write(date_time + "\n")
        
            file.write("\n")
 
            file.write(entry + "\n")

            file.write("\n")
        
        print("Entry added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()