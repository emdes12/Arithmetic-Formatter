def arithmetic_arranger(problems, show_answers=False):
    if not len(problems) <= 5:
        return print("Error: Too many problems.")
    
    upper_rows = None
    lower_rows = None
    eqautor = None
    solv = None
    for prob in problems:
        prob_split = prob.split()
        if len(prob_split[0]) > 4 or len(prob_split[2]) > 4:
            return print("Error: Numbers cannot be more than four digits.")
        if not prob_split[1] == "+" and not prob_split[1] == "-":
            return print("Error: Operator must be '+' or '-'.")
        try:
            int(prob_split[0]) and int(prob_split[2])
        except:
            return print("Error: Numbers must only contain digits.")

        uppers = ""
        lowers = []
        space = max([len(prob_split[0]), len(prob_split[2])]) + 1

        if len(prob_split[0]) < space:
            sp_to_add = space - len(prob_split[0])
            
            ng_sp = " " * sp_to_add
            uppers = ng_sp + prob_split[0]
            
        if len(prob_split[2]) < space:
            sp_to_add = space - len(prob_split[2])
            ng_sp = ''
            ng_sp += " " * sp_to_add
            lowers = ng_sp + prob_split[2]
            
        
        if upper_rows is None:
            upper_rows = " " + uppers
        else:
            upper_rows += "     " + uppers
        
        if lower_rows is None:
            lower_rows = prob_split[1] + lowers
        else:
            lower_rows += "    " + prob_split[1] +  lowers
        
        dv_nm = space + 1
        divds = "-" * dv_nm
        if eqautor is None:
            eqautor = divds
        else:
            eqautor += "    " + divds
        
        ans = str(eval(prob))
        
        str_ans = ""
        if '-' in ans:
            if len(ans) < space + 1 :
                sp_to_add = space - len(ans)
                ng_sp = ''
                ng_sp += " " * sp_to_add
                str_ans = ng_sp + ans
        elif len(ans) < space :
            sp_to_add = space - len(ans)
            ng_sp = ''
            ng_sp += " " * sp_to_add
            str_ans = ng_sp + ans
        else:
            str_ans = ans
        
            
        if solv is None:
            solv = " " + str_ans
        else:
            solv += "     " + str_ans
        
        submit = ""
        
        if show_answers:
            submit = f"{upper_rows}\n{lower_rows}\n{eqautor}\n{solv}"
        else:
            submit = f"{upper_rows}\n{lower_rows}\n{eqautor}"
        

    return submit



print(f'\n{arithmetic_arranger(["98 + 35", "3801 - 2", "45 + 43", "123 + 49"], True)}')