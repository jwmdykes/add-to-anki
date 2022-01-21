;CapsLock + c - Run python program to add to anki deck
CapsLock & c::
    CoordMode, Mouse, Screen    
    MouseGetPos, xpos, ypos
    ; MsgBox, The cursor is at X%xpos% Y%ypos%. ; for testing that the coordinates are right
    Run C:/Users/98joh/AppData/Local/Programs/Python/Python310/pythonw.exe c:/code/add-to-anki/main.pyw %xpos% %ypos%
    sleep, 200
    if WinExist("Input a Korean English pair")
        WinActivate
