def EditSourceCode(SourceCode):
  while True:
    LineNumber = int(input("Enter line number of code to edit: "))
    print(SourceCode[LineNumber])
    Choice = input("E - Edit this line\nC - Cancel edit\nEnter your choice: ").upper()
    if Choice == "C":
      break
    NewLabel = input("Input a new LABEL (input NOTHING if no label): ").replace(" ", "")
    NewOpcode = input("Input a new OPCODE (input NOTHING if no opcode): ").replace(" ", "")
    NewOperand = input("Input a new OPERAND (input NOTHING if no operand): ").replace(" ", "")
    NewLabel += ":" if NewLabel != "" and ":" not in NewLabel else ""
    Line = f"{NewLabel:6} {NewOpcode:5} {NewOperand}"
    SourceCode[LineNumber] = Line
    DisplaySourceCode(SourceCode)
  return SourceCode
