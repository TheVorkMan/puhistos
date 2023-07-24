#include <windows.h>

int main()
{
    HMODULE hModule = GetModuleHandle(NULL);
    HRSRC hResource = FindResource(hModule, MAKEINTRESOURCE(IDR_MY_RESOURCE), RT_RCDATA);
    HGLOBAL hMemory = LoadResource(hModule, hResource);
    DWORD dwSize = SizeofResource(hModule, hResource);
    LPVOID lpResourceData = LockResource(hMemory);

// Дальше можно использовать lpResourceData для работы с данными ресурса.
    
    UnlockResource(hMemory);
    FreeResource(hMemory);
    
    return 0;
}