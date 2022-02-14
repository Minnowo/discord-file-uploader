#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%

CoordMode, Mouse, Screen
SetTimer, Check, 20

originalContext := DllCall("SetThreadDpiAwarenessContext", "ptr", -3, "ptr")

msgbox, use ctrl + space to show coords in a messagebox | use escape to close  | close this msgbox for DPI awarness to work 
return

Check:
    MouseGetPos, xx, yy
    Tooltip %xx% %yy%
    return

^space::
    msgbox, %xx%`, %yy%
    return


Esc::ExitApp