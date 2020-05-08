chocopySyntax = {
    'nt_literal': {
        'kw_NONE',
        'kw_True',
        'kw_False',
        'tk_entero',
        'tk_id',
        'tk_cadena'},

    'nt_expr':{
        'nt_cexpr',
        'kw_not nt_expr',
        'nt_expr nt_expr1 nt_expr',
        'nt_expr kw_if nt_expr kw_else nt_expr'},

    'nt_expr1':{
        'kw_and',
        'kw_or'
    },
    'nt_cexpr':{
        'tk_id',
        'nt_literal',
        'tk_llave_izq nt_cexpr1 tk_llave_der',
        'tk_par_izq nt_expr tk_par_der',
        'nt_member_expr',
        'nt_index_expr',
        'nt_member_expr tk_par_izq nt_cexpr1 tk_par_der',
        'tk_id tk_par_izq nt_cexpr1 tk_par_der',
        'nt_cexpr nt_bin_op nt_cexpr',
        'tk_res nt_cexpr'},
    'nt_cexpr1':{
        'nt_expr nt_cexpr1.1'
    },
    'nt_cexpr1.1':{
        'tk_coma nt_expr nt_cexpr1.1',
        'e'
    },
    'nt_bin_op':{
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
    },
    'nt_member_expr': {
        'nt_cexpr tk_punto tk_div'
    },
    'nt_index_expr':{
        'nt_cexpr tk_llave_izq nt_expr tk_llave_der'
    },
    'nt_target':{
        'tk_id',
        'nt_member_expr',
        'nt_index_expr'
    }
}
print(chocopySyntax)