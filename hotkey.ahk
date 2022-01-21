;CapsLock + c - Run python program to add to anki deck
CapsLock & c::
    CoordMode, Mouse, Screen    
    MouseGetPos, xpos, ypos
    ; Set working directory so that paths work correctly before calling the script
    ; Would be better to find another solution to this
    SetWorkingDir, C:/code/add-to-anki/ 
    Run C:/Users/98joh/AppData/Local/Programs/Python/Python310/pythonw.exe main.pyw %xpos% %ypos%
    sleep, 1000
    if WinExist("Input a Korean English pair")
        WinActivate

