#Persistent
#NoTrayIcon
setbatchlines -1
sendmode input
setkeydelay -1

args := 0
for n, param in A_Args
    args++

if(args = 1)
{
    send, {%1%}
}
exitapp 