import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_count = (accounts['income']<20000).sum()
    ## case 2
    # low_count = len(accounts[accounts['income'] < 20000])
    average_count = ((accounts['income']>=20000) & (accounts['income']<=50000)).sum()
    
    high_count = (accounts['income']>50000).sum()
    ans = pd.DataFrame({'category': ['Low Salary','Average Salary','High Salary'],
                        "accounts_count": [low_count,average_count,high_count]})
    return ans
