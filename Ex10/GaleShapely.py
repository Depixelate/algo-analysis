def GaleShapely(scholar_prefs, advisor_prefs):
    n = len(scholar_prefs)
    advisor_to_scholar = [-1 for i in range(n)]
    scholar_cur_pref = [1 for i in range(n)]
    
    for i in range(n):
        cur_scholar = i
        while cur_scholar != -1:
            cur_pref = scholar_cur_pref[cur_scholar]
            scholar_cur_pref[cur_scholar] += 1
            advisor = scholar_prefs[cur_scholar].index(cur_pref)
            paired_scholar = advisor_to_scholar[advisor]
            if paired_scholar == -1 or advisor_prefs[advisor][cur_scholar] < advisor_prefs[advisor][paired_scholar]:
                advisor_to_scholar[advisor] = cur_scholar
                cur_scholar = paired_scholar
    
    return advisor_to_scholar

def main():
    n = int(input("Enter the number of scholars and advisors: "))
    scholar_prefs = [eval(input(f"Enter the preference order for scholar {i+1}: ")) for i in range(n)]
    advisor_prefs = [eval(input(f"Enter the preference order for advisor {i+1}: ")) for i in range(n)]
    adv_to_schol = GaleShapely(scholar_prefs, advisor_prefs)
    for i in range(n):
        print(f"Advisor {i+1}: Scholar {adv_to_schol[i]+1}")
     
        

if __name__ == "__main__":
    main()