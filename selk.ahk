#SingleInstance, force
SetTitleMatchMode, 2
Run cmd.exe /k title ahkz,,min
WinWait, ahkz,,1
ControlSend,,py{Enter},ahkz
Sleep, 1000   
ControlSend,,selp="x"{Enter},ahkz
a=exec ( open ( r"D:\Gits\SmartPy\sel-.py" ) .read (  )  ) `;
ControlSend,,%a%{Enter},ahkz
a=os .system ( r"subl D:\Gits\SmartPy\selq.py" ) `;
ControlSend,,%a%{Enter},ahkz

