import platform
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import warnings
# warnings.filterwarnings('ignore')


from matplotlib import font_manager, rc


def bar():
    plt.rcParams['font.size'] = 10.0
    plt.rcParams['font.family'] = 'Malgun Gothic'
    if platform.system() == 'Windows':
        path = 'c:/Windows/Fonts/malgun.ttf'
        font_name = font_manager.FontProperties(fname=path).get_name()
        rc('font', family=font_name)
    elif platform.system() == 'Darwin':
        rc('font', family='AppleGothic')
    else:
        print('Check your OS system')

    df = pd.read_excel('./files/youtube_rank.xlsx')
    df['replaced_view'] = df['view'].str.replace('억', '')
    df['replaced_view'] = df['replaced_view'].str.replace('만', '0000')

    df['replaced_view'] = df['replaced_view'].astype('int64')

    # pivot category 별 viewer
    pivot2_df = df.pivot_table(
        index='category', values='replaced_view', aggfunc=['sum', 'count'])

    print('-----------1-----------')
    pivot2_df.columns = ['view_sum', 'category_count']

    print('-----------2-----------')
    pivot2_df['category'] = pivot2_df.index
    print('-----------3-----------')
    print(pivot2_df)

    chart = sns.catplot(x='view_sum', y='category', data=pivot2_df, kind='bar')
    chart.savefig("./static/image/barchart2212")
    print("----4-------")
    # plt.figure(figsize=(30, 30))
    # plt.pie(pivot2_df['view_sum'],
    #         labels=pivot2_df['category'], autopct='%1.1f%%')

    # plt.figure(figsize=(600, 800))

    print('-----------5-----------')

    return "ddd"  # 함의 함수와 상관 없는 결과라도 연결 여부를 알기 위해 아무 문자나 대입 해서 확인할 수 있다.


# if __name__ == "__main__":
#     bar()
