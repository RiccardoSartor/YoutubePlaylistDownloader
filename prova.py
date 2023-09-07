import win32clipboard as clip

clip.OpenClipboard()
data = clip.GetClipboardData()
clip.CloseClipboard()

print(data)

