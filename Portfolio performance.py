# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:56:19 2021

@author: Richard
"""



# =============================================================================

# #measure correlation
st_rev_RE_IND =mom_daily_ret_RE.to_frame().merge(mom_daily_ret_IND.rename("IND"), how="outer",left_index = True, right_index=True)
st_rev_RE_IND = st_rev_RE_IND.dropna(how='all').fillna(0)
plt.scatter(st_rev_RE_IND.iloc[:,0],st_rev_RE_IND.iloc[:,1])
np.corrcoef(st_rev_RE_IND.iloc[:,0],st_rev_RE_IND.iloc[:,1])
stats.pearsonr(st_rev_RE_IND.iloc[:,0],st_rev_RE_IND.iloc[:,1])

comb = (st_rev_RE_IND.iloc[:,0] + st_rev_RE_IND.iloc[:,1])/2
cum_comb =(1+comb).cumprod()
plt.plot(cum_comb)

print('combined')
print(cum_comb.tail(1)**(1/7)-1)
print(comb.std()*math.sqrt(252))
print((cum_comb.tail(1)**(1/7)-1)/(comb.std()*math.sqrt(252)))
print((cum_comb.tail(1)**(1/7)-1)/(comb.std()*math.sqrt(252))**2)

#maxiumum drawdown
comb_Roll_Max = cum_comb.cummax()
comb_Daily_Drawdown = cum_comb/comb_Roll_Max - 1.0
comb_Max_Daily_Drawdown = comb_Daily_Drawdown.cummin()
print(comb_Max_Daily_Drawdown.tail(1))
# =============================================================================
