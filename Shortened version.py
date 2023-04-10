def EditSourceCode(SourceCode):
    line_num = int(input("Enter line number of code to edit: "))
    print(SourceCode[line_num])
    while True:
        choice = input("E - Edit this line\nC - Cancel edit\nEnter your choice: ").upper()
        if choice == "C":
            break
        elif choice == "E":
            new_label = input("Input a new LABEL (input NOTHING if no label): ").strip(":").ljust(6)
            new_opcode = input("Input a new OPCODE (input NOTHING if no opcode): ").ljust(5)
            new_operand = input("Input a new OPERAND (input NOTHING if no operand): ").ljust(10)
            SourceCode[line_num] = new_label + " " + new_opcode + new_operand
            print(SourceCode)
    return SourceCode
