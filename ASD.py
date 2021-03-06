chocopySyntax = {
    # program ::= [var def | func def | class def]^∗ stmt^∗

    'nt_program':[
        'nt_inicio_def nt_inicio_stmt',
    ],

    'nt_inicio_def':[
        'nt_var_def nt_inicio_def',
        'nt_func_def nt_inicio_def',
        'nt_class_def nt_inicio_def',
        'e'
    ],

    'nt_inicio_stmt':[
        'nt_stmt nt_inicio_stmt',
        'e'
    ],

    # class def ::= class ID ( ID ) : NEWLINE INDENT class body DEDENT

    'nt_class_def':[
        'kw_class tk_id tk_par_izq tk_id tk_par_der NEWLINE INDENT nt_class_body DEDENT',
    ],

    # class_body ::= pass NEWLINE | [ var def | func def ]^+

    'nt_class_body':[
        'kw_pass NEW_LINE',
        'nt_var_def nt_aux_def',
        'nt_func_def nt_aux_def'
    ],

    'nt_aux_def':[
        'nt_var_def nt_aux_def',
        'nt_func_def nt_aux_def',
        'e'
    ],

    # func_def ::= def ID ( [typed_var [, typed_var]^∗]^? ) [-> type ]^? : NEWLINE INDENT func_body DEDENT    

    'nt_func_def':[
        'kw_def tk_id tk_par_izq nt_argument_aux tk_par_der nt_return_aux tk_dospuntos NEWLINE INDENT nt_func_body DEDENT'
    ],

    'nt_argument_aux':[
       'nt_typed_var nt_nvars_aux',
       'e'
    ],

    'nt_nvars_aux':[
        'tk_coma nt_typed_var nt_nvars_aux',
        'e'
    ],
    
    'nt_return_aux':[
        'tk_ejecuta nt_type',
        'e'
    ],

    # func_body ::= [global_decl | nonlocal_decl | var_def | func_def ]^* stmt^+

    'nt_func_body':[
        'nt_decl_def_aux nt_stmt nt_nstmt_aux'
    ],

    'nt_decl_def_aux':[
        'nt_global_decl nt_decl_def_aux',
        'nt_nonlocal_decl nt_decl_def_aux',
        'nt_var_def nt_decl_def_aux',
        'nt_func_def nt_decl_def_aux',
        'e',
    ],

    'nt_nstmt_aux':[
        'nt_stmt nt_nstmt_aux',
        'e'
    ],

    # typed_var ::= ID : type

    'nt_typed_var':[
        'tk_id tk_dospuntos nt_type'
    ],

    # type ::= ID | IDSTRING | '[' type ']'

    'nt_type':[
        'tk_id',
        'tk_idstring',
        'tk_llave_izq nt_type tk_llave_der'
    ],

    # global decl ::= global ID NEWLINE

    'nt_global_decl':[
        'kw_global tk_id NEWLINE'
    ],

    # nonlocal decl ::= nonlocal ID NEWLINE

    'nt_nonlocal_decl':[
        'kw_nonlocal tk_id NEWLINE'
    ],

    # var_def ::= typed_var = literal NEWLINE

    'nt_var_def':[
        'nt_typed_var tk_asig nt_literal NEWLINE'
    ],

    # stmt ::= simple_stmt NEWLINE | if expr : block [elif expr : block ]^* [else : block]^? | while expr : block | for ID in expr : block

    'nt_stmt':[
        'nt_simple_stmt NEWLINE',
        'kw_if nt_expr tk_dospuntos nt_block nt_ncond_aux nt_fcond_aux',
        'kw_while nt_expr tk_dospuntos nt_block',
        'kw_for tk_id kw_in nt_expr tk_dospuntos nt_block'
    ],

    'nt_ncond_aux':[
        'kw_elif nt_expr tk_dospuntos nt_block nt_ncond_aux',
        'e'
    ],

    'nt_fcond_aux':[
        'kw_else tk_dospuntos nt_block',
        'e'
    ],

    # simple stmt ::= pass | expr | return [expr]^? | [ target = ]^+ expr

    'nt_simple_stmt':[
        'kw_pass',
        'nt_expr',
        'kw_return nt_expr_aux',
        'nt_target tk_asig nt_ntargets_aux nt_expr'

    ],

    'nt_expr_aux':[
        'nt_expr',
        'e'
    ],

    'nt_ntargets_aux':[
        'nt_target tk_asig nt_ntargets_aux',
        'e'
    ],

    # block ::= NEWLINE INDENT stmt+ DEDENT

    'nt_block':[
        'NEWLINE INDENT nt_stmt nt_nstmt_aux DEDENT'
    ],

    # literal ::= None | True | False | INTEGER | IDSTRING | STRING

    'nt_literal': [
        'kw_None',
        'kw_True',
        'kw_False',
        'tk_entero',
        'tk_id',
        'tk_cadena'
    ],

    # expr ::= cexpr | not expr | expr [and | or] expr | expr if expr else expr

    'nt_expr':[
        'nt_cexpr',
        'kw_not nt_expr',
        'nt_expr nt_expr1 nt_expr',
        'nt_expr kw_if nt_expr kw_else nt_expr'
    ],
    'nt_expr':[
        'nt_cexpr nt_expr2',
        'kw_not nt_expr nt_expr2',
    ],
    'nt_expr2':[
        'nt_expr1 nt_expr nt_expr2',
        'kw_if nt_expr kw_else nt_expr nt_expr2',
        'e'
    ],
    
    'nt_expr1':[
        'kw_and',
        'kw_or'
    ],

    # cexpr ::= ID | literal | '['  [expr[, expr]^*]^?  ']' | ( expr ) | member_expr | index_expr | member_expr (  [expr [, expr]^*]^?  )
    #              | ID  (  [expr [, expr]^*]^?  )  | cexpr bin_op cexpr | - cexpr

    'nt_cexpr':[
        'tk_id nt_cexpr2',
        'nt_literal nt_cexpr2',
        'tk_llave_izq nt_cexpr1 tk_llave_der nt_cexpr2',
        'tk_par_izq nt_expr tk_par_der nt_cexpr2',
        'nt_member_expr nt_cexpr2',
        'nt_index_expr nt_cexpr2',
        'nt_member_expr tk_par_izq nt_cexpr1 tk_par_der nt_cexpr2',
        'tk_id tk_par_izq nt_cexpr1 tk_par_der nt_cexpr2',
        'tk_res nt_cexpr nt_cexpr2'
    ],
    'nt_cexpr2':[
        'nt_bin_op nt_cexpr nt_cexpr2',
        'e'
    ],


    'nt_cexpr1':[
        'nt_expr nt_cexpr1.1',
        'e'
    ],

    'nt_cexpr1.1':[
        'tk_coma nt_expr nt_cexpr1.1',
        'e'
    ],

    # bin_op ::= + | - | * | // | % | == | != | <= | >= | < | > | is

    'nt_bin_op':[
        'tk_sum',
        'tk_res',
        'tk_mul',
        'tk_div',
        'tk_mod',
        'tk_igual',
        'tk_diferente',
        'tk_menorig',
        'tk_mayorig',
        'tk_menor',
        'tk_mayor',
        'kw_is'
    ],

    # member_expr ::= cexpr . ID

    'nt_member_expr': [
        'nt_cexpr tk_punto tk_id'
    ],

    # index_expr ::= cexpr '[' expr ']'

    'nt_index_expr':[
        'nt_cexpr tk_llave_izq nt_expr tk_llave_der'
    ],

    # target ::= ID

    'nt_target':[
        'tk_id',
        'nt_member_expr',
        'nt_index_expr'
    ]
}

otro = {'nt_A': ['nt_B nt_C', 'kw_bad'],     
        'nt_B': ['kw_big nt_C kw_boss','e'],
        'nt_C': ['kw_cat','kw_cow'],
}
hoffman = {
    'nt_A': [
        'nt_B nt_C',
        'kw_ant nt_A kw_all'
    ],
    'nt_B': [
        'kw_big nt_C',
        'kw_bus nt_A kw_boss',
        'e'
    ],
    'nt_C': [
        'kw_cat',
        'kw_cow'
    ]
}
firsts_list = {}
for i in list(otro.keys()):
    firsts_list[i] = set()

def aux_calc(alpha,grammar,visited):
    #print(alpha)
    if (alpha == 'e') or (alpha[:2]!='nt'): return [alpha.split(' ')[0]]
    else:
        cur_symbol = alpha.split(' ')[0]
        visited.append(cur_symbol)
        has_epsilon = 'e' in grammar[cur_symbol]
        aux_set = set()

        for next_alpha in grammar[cur_symbol]:
            if next_alpha.split(' ')[0] not in visited:
                aux_set.update(aux_calc(next_alpha,grammar,visited))
        
        aux_set = aux_set.difference('e')

        if has_epsilon:
            if len(alpha.split(' ')) == 1:
                aux_set.add('e')
            else:
                aux_set.update(aux_calc(alpha.split(' ')[1],grammar,visited))
        
        return aux_set

def calc_first(grammar):
    #dict with empty sets
    firsts_list = {}
    for i in list(grammar.keys()):
        firsts_list[i] = set()

    for symbol, rules in grammar.items():
        for alpha in rules:
            firsts_list[symbol].update(aux_calc(alpha,grammar,[]))
            
    
    return firsts_list


first = calc_first(hoffman)

for key,values in first.items():
    print(key, values,sep=' -> ', end='\n')