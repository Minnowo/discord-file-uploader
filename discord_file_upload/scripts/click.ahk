#Persistent
#NoTrayIcon
setbatchlines -1
sendmode input
setkeydelay -1
CoordMode, Mouse, Screen

args := 0
for n, param in A_Args
    args++

if(args = 2)
{
    originalContext := DllCall("SetThreadDpiAwarenessContext", "ptr", -3, "ptr")
    click, %1% , %2% 
}
exitapp 