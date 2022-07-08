Add-Type @"
using System;
using System.Runtime.InteropServices;

public class winuser
{
    [DllImport("User32.dll")]
    public static extern bool BlockInput(bool fBlockIt);
}
"@

[winuser]::BlockInput($true)

Start-Process -NoNewWindow -Wait "withheld-editable.bat"

[winuser]::BlockInput($false)
