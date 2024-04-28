def create_list_from_file(file_name):
    lines = []

    with open(file_name,"r") as file:
        lines = [line.strip("\n") for line in file.readlines()]
                 
    return lines



if __name__ ==  "__main__":
   file_name = input("Please enter a file name: ")
   try:
      lines = create_list_from_file(file_name)

      while True:
          print(f"\nNumber of lines in the file {file_name}: {len(lines)}") 
          line_no = int(input("Please enter a line number:"))

          if line_no == 0:
             print(" Exiting ")
             break

          if line_no > len(lines):
             print("Invalid line number entered! Please try again.")
          else:
              print(f"Value at line {line_no}: {lines[line_no - 1]}")
   except FileNotFoundError as e:
        print(e)                                