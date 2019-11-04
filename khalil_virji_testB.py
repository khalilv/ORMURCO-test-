# RETURN -1 if ver1 < ver2
# RETURN 1 if ver1 > ver2
# RETURN 0 if ver1 == ver2
# RETURN "error" if error
# ASSUME ver1 and ver2 are two version strings. If not report error.


def compare2V(ver1, ver2):
    arr1 = ver1.split(".")
    arr2 = ver2.split(".")
    if len(arr1) != 2 or len(arr2) != 2:
        return "error"
    i = 0
    while i < len(arr1):
        if arr1[i] > arr2[i]:
            return 1
        if arr1[i] < arr2[i]:
            return -1
        i = i+1
    return 0
