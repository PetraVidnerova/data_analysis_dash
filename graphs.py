import plotly.graph_objs as go
from plotly import tools
import pandas as pd


# read the data 
students = pd.read_csv('students.csv')

# for each graph define a function and string with code
def hist_age():
    girls = go.Histogram(
        x = students[students['sex'] == 'F'].age,
        name = 'dívky')
    boys = go.Histogram(
        x = students[students['sex'] == 'M'].age,
        name = 'chlapci')

    figure={
        'data': [girls, boys],
        'layout': {
            'title': 'Histogram rozdělení věku - chlapci, dívky',
            'xaxis': { 'title': 'věk'}
        }
    }

    return figure

hist_age_txt = ''' 
```
    girls = go.Histogram(
        x = students[students['sex'] == 'F'].age,
        name = 'dívky')
    boys = go.Histogram(
        x = students[students['sex'] == 'M'].age,
        name = 'chlapci')

    figure={
        'data': [girls, boys],
        'layout': {
            'title': 'Histogram rozdělení věku - chlapci, dívky',
            'xaxis': { 'title': 'věk'}
        }
    }

```
'''

def alcohol_bar():
    trace1 = students[(students['sex'] == 'F') & (students['age']<20)][['age', 'Aalc']].groupby('age').mean()
    trace2 = students[(students['sex'] == 'M') & (students['age']<20)][['age', 'Aalc']].groupby('age').mean() 
    trace3 = students[students.age < 20][['age','Aalc']].groupby('age').mean()

    girls = go.Bar(
        x = trace1.index,
        y = trace1.Aalc,
        name = 'Dívky')

    boys = go.Bar(
        x = trace2.index,
        y = trace2.Aalc, 
        name = 'Chlapci')

    both = go.Bar(
        x = trace3.index,
        y = trace3.Aalc,
        name = 'Všichni')

    layout = go.Layout(
        title = 'Průměrná konzumace alkoholu',
        yaxis = dict(range=[1,2.5], title='1 (nízká spotřeba) - 5 (vysoká spotřeba)'),
        xaxis = dict(title='věk'))

    fig = dict(data=[girls, boys, both], layout=layout)
    return fig

alcohol_bar_txt = '''
```
    trace1 = students[(students['sex'] == 'F') & (students['age']<20)][['age', 'Aalc']].groupby('age').mean()
    trace2 = students[(students['sex'] == 'M') & (students['age']<20)][['age', 'Aalc']].groupby('age').mean() 
    trace3 = students[students.age < 20][['age','Aalc']].groupby('age').mean()

    girls = go.Bar(
        x = trace1.index,
        y = trace1.Aalc,
        name = 'Dívky')

    boys = go.Bar(
        x = trace2.index,
        y = trace2.Aalc, 
        name = 'Chlapci')

    both = go.Bar(
        x = trace3.index,
        y = trace3.Aalc,
        name = 'Všichni')

    layout = go.Layout(
        title = 'Průměrná konzumace alkoholu',
        yaxis = dict(range=[1,2.5], title='1 (nízká spotřeba) - 5 (vysoká spotřeba)'),
        xaxis = dict(title='věk'))

    fig = dict(data=[girls, boys, both], layout=layout)
```
'''

def alcohol_box():
    
    data = []

    for age in range(15, 23):
        trace = go.Box(
            y = students[students.age == age].Aalc,
            name = '{}({})'.format(age, sum(students.age == age)),
            boxpoints = 'outliers')
        data.append(trace)
    
    layout = go.Layout(
        title="Konzumace alkoholu dle věku",
        yaxis = dict(title='1 (nízká spotřeba) - 5 (vysoká spotřeba)'),
        xaxis = dict(title='věk(#vzorků)'))

    fig = dict(data=data, layout=layout)
    return fig 


alcohol_box_txt = '''
```
    data = []

    for age in range(15, 23):
        trace = go.Box(
            y = students[students.age == age].Aalc,
            name = '{}({})'.format(age, sum(students.age == age)),
            boxpoints = 'outliers')
        data.append(trace)
    
    layout = go.Layout(
        title="Konzumace alkoholu dle věku",
        yaxis = dict(title='1 (nízká spotřeba) - 5 (vysoká spotřeba)'),
        xaxis = dict(title='věk(#vzorků)'))

    fig = dict(data=data, layout=layout)
```
'''

def alcohol_family():
    background_alc = students.groupby('famrel').Aalc.mean()
    data = go.Scatter(
        x = background_alc.index,
        y = background_alc,
        mode = 'lines')

    layout = go.Layout(
        title = 'Rodinné zázemí a alkohol',
        xaxis = dict(title='rodinné zázemí 1 (špatné) - 5 (vynikající)'),
        yaxis = dict(title='konzumace alkoholu 1-5'))

    fig = dict(data=[data], layout=layout)
    return fig

alcohol_family_txt = '''
```
    background_alc = students.groupby('famrel').Aalc.mean()
    data = go.Scatter(
        x = background_alc.index,
        y = background_alc,
        mode = 'lines')

    layout = go.Layout(
        title = 'Rodinné zázemí a alkohol',
        xaxis = dict(title='rodinné zázemí 1 (špatné) - 5 (vynikající)'),
        yaxis = dict(title='konzumace alkoholu 1-5'))

    fig = dict(data=[data], layout=layout)
```
'''


def internet_lifestyle():

    # going out with friends 
    i_access = go.Box(
        y = students[students.internet].goout,
        name = "internet doma",
        marker = dict(color='blue')
    )
    no_i_access = go.Box(
        y = students[students.internet == False].goout,
        name = "bez internetu",
        marker = dict(color='orange'))

    goout = [i_access, no_i_access]


    # free time
    i_access = go.Box(
        y = students[students.internet].freetime,
        name = "internet doma",
        marker = dict(color='blue'))
    no_i_access = go.Box(
        y = students[students.internet == False].freetime,
        name = "bez internetu",
        marker = dict(color='orange'))
    
    freetime = [i_access, no_i_access]

    # romantic relation ship 
    internet = students[students.internet == True].groupby('romantic').age.count()/len(students[students.internet == True])
    no_internet = students[students.internet == False].groupby('romantic').age.count()/len(students[students.internet == False])

    i_access = go.Bar(
        x = ['single', 've vztahu'],
        y = 100*internet,
        name = "internet doma",
        marker = dict(color='blue'))
    no_i_access = go.Bar(
        x = ['single', 've vztahu'],
        y = 100*no_internet,
        name = "bez internetu",
        marker = dict(color='orange'))

    romantic = [i_access, no_i_access]

    # family relation ship
    i_access = go.Box(
        y = students[students.internet == True].famrel,
        name = "internet doma",
        marker = dict(color='blue'))
    no_i_access = go.Box(
        y = students[students.internet == False].famrel,
        name = "bez internetu",
        marker = dict(color='orange'))
    
    famrel = [i_access, no_i_access]

    # graph
    fig = tools.make_subplots(rows=1, cols=4, subplot_titles=('Chození ven', 'Volný čas',
                                                          'Vztahy', 'Rodinné zázemí'))

    fig.append_trace(goout[0], 1, 1)
    fig.append_trace(goout[1], 1, 1)
    
    fig.append_trace(freetime[0], 1, 2)
    fig.append_trace(freetime[1], 1, 2)
    
    fig.append_trace(romantic[0], 1, 3)
    fig.append_trace(romantic[1], 1, 3)
    
    fig.append_trace(famrel[0], 1, 4)
    fig.append_trace(famrel[1], 1, 4)

    fig['layout'].update( title='Přístup k internetu a životní styl', showlegend=False)
    fig['layout']['yaxis1'].update(title='1 (málo) - 5 (hodně)')
    fig['layout']['yaxis2'].update(title='1 (málo) - 5 (hodně)')
    fig['layout']['yaxis3'].update(title='%')
    fig['layout']['yaxis4'].update(title='1 (špatné) - 5 (vynikající)')
    return fig

internet_lifestyle_txt = '''
```
    # going out with friends 
    i_access = go.Box(
        y = students[students.internet].goout,
        name = "internet doma",
        marker = dict(color='blue')
    )
    no_i_access = go.Box(
        y = students[students.internet == False].goout,
        name = "bez internetu",
        marker = dict(color='orange'))

    goout = [i_access, no_i_access]


    # free time
    i_access = go.Box(
        y = students[students.internet].freetime,
        name = "internet doma",
        marker = dict(color='blue'))
    no_i_access = go.Box(
        y = students[students.internet == False].freetime,
        name = "bez internetu",
        marker = dict(color='orange'))
    
    freetime = [i_access, no_i_access]

    # romantic relation ship 
    internet = students[students.internet == True].groupby('romantic').age.count()/len(students[students.internet == True])
    no_internet = students[students.internet == False].groupby('romantic').age.count()/len(students[students.internet == False])

    i_access = go.Bar(
        x = ['single', 've vztahu'],
        y = 100*internet,
        name = "internet doma",
        marker = dict(color='blue'))
    no_i_access = go.Bar(
        x = ['single', 've vztahu'],
        y = 100*no_internet,
        name = "bez internetu",
        marker = dict(color='orange'))

    romantic = [i_access, no_i_access]

    # family relation ship
    i_access = go.Box(
        y = students[students.internet == True].famrel,
        name = "internet doma",
        marker = dict(color='blue'))
    no_i_access = go.Box(
        y = students[students.internet == False].famrel,
        name = "bez internetu",
        marker = dict(color='orange'))
    
    famrel = [i_access, no_i_access]

    # graph
    fig = tools.make_subplots(rows=1, cols=4, subplot_titles=('Chození ven', 'Volný čas',
                                                          'Vztahy', 'Rodinné zázemí'))

    fig.append_trace(goout[0], 1, 1)
    fig.append_trace(goout[1], 1, 1)
    
    fig.append_trace(freetime[0], 1, 2)
    fig.append_trace(freetime[1], 1, 2)
    
    fig.append_trace(romantic[0], 1, 3)
    fig.append_trace(romantic[1], 1, 3)
    
    fig.append_trace(famrel[0], 1, 4)
    fig.append_trace(famrel[1], 1, 4)

    fig['layout'].update( title='Přístup k internetu a životní styl', showlegend=False)
    fig['layout']['yaxis1'].update(title='1 (málo) - 5 (hodně)')
    fig['layout']['yaxis2'].update(title='1 (málo) - 5 (hodně)')
    fig['layout']['yaxis3'].update(title='%')
    fig['layout']['yaxis4'].update(title='1 (špatné) - 5 (vynikající)')
```
'''



def relationship_age():
    girls = students[(students['sex'] == 'F') & (students['age']<20)]
    boys = students[(students['sex'] == 'M') & (students['age']<20)]
    girls_perc = 100*girls.groupby('age').romantic.sum()/girls.groupby('age').romantic.count()
    boys_perc = 100*boys.groupby('age').romantic.sum()/boys.groupby('age').romantic.count()

    girls_bar = go.Bar(
        x = girls_perc.index,
        y = girls_perc,
        name = "dívky")
    boys_bar = go.Bar(
        x = girls_perc.index,
        y = boys_perc,
        name = 'chlapci')
    layout = go.Layout(
        title = 'Vztahy a věk',
        xaxis = dict(title='věk'),
        yaxis = dict(title='% ve vztahu'))

    fig = dict(data=[girls_bar, boys_bar], layout=layout)
    return fig 

relationship_age_txt = '''
```
    girls = students[(students['sex'] == 'F') & (students['age']<20)]
    boys = students[(students['sex'] == 'M') & (students['age']<20)]
    girls_perc = 100*girls.groupby('age').romantic.sum()/girls.groupby('age').romantic.count()
    boys_perc = 100*boys.groupby('age').romantic.sum()/boys.groupby('age').romantic.count()

    girls_bar = go.Bar(
        x = girls_perc.index,
        y = girls_perc,
        name = "dívky")
    boys_bar = go.Bar(
        x = girls_perc.index,
        y = boys_perc,
        name = 'chlapci')
    layout = go.Layout(
        title = 'Vztahy a věk',
        xaxis = dict(title='věk'),
        yaxis = dict(title='% ve vztahu'))

    fig = dict(data=[girls_bar, boys_bar], layout=layout)
```
'''



def mother_box():
    mother = students[['Mjob', 'famrel']]

    trace1 = go.Box(
        y = mother[mother.Mjob == 'at_home'].famrel,
        name = 'V domácnosti',
        boxpoints = 'all')
    trace2 = go.Box(
        y = mother[mother.Mjob != 'at_home'].famrel,
        name = 'Pracující',
        boxpoints = 'all')

    layout = go.Layout(
        title="Pracující matky a rodinné zázemí",
        yaxis=dict(title="rodinné zázemí 1 (špatné) - 5 (vynikající)")
    )

    fig = dict(data=[trace1, trace2], layout=layout)

    return fig

mother_box_txt = '''
```
    mother = students[['Mjob', 'famrel']]

    trace1 = go.Box(
        y = mother[mother.Mjob == 'at_home'].famrel,
        name = 'V domácnosti',
        boxpoints = 'all')
    trace2 = go.Box(
        y = mother[mother.Mjob != 'at_home'].famrel,
        name = 'Pracující',
        boxpoints = 'all')

    layout = go.Layout(
        title="Pracující matky a rodinné zázemí",
        yaxis=dict(title="rodinné zázemí 1 (špatné) - 5 (vynikající)")
    )

    fig = dict(data=[trace1, trace2], layout=layout)
```
'''


def mother_hist():
    mother = students[['Mjob', 'famrel']]
    
    trace1 = go.Histogram(
        x = mother[mother.Mjob == 'at_home'].famrel,
        opacity = 0.75,
        name = 'V domácnosti')
    trace2 = go.Histogram(
        x = mother[mother.Mjob != 'at_home'].famrel,
        opacity = 0.75,
        name = 'Pracující')

    layout = go.Layout(
        title = "Pracující matky a rodinné zázemí",
        barmode = 'overlay',
        xaxis = dict(title='rodinné zázemí 1 (špatné) - 5 (vynikající)')
    )
    fig = dict(data=[trace2, trace1], layout=layout)

    return fig

mother_hist_txt = '''
```
    mother = students[['Mjob', 'famrel']]
    
    trace1 = go.Histogram(
        x = mother[mother.Mjob == 'at_home'].famrel,
        opacity = 0.75,
        name = 'V domácnosti')
    trace2 = go.Histogram(
        x = mother[mother.Mjob != 'at_home'].famrel,
        opacity = 0.75,
        name = 'Pracující')

    layout = go.Layout(
        title = "Pracující matky a rodinné zázemí",
        barmode = 'overlay',
        xaxis = dict(title='rodinné zázemí 1 (špatné) - 5 (vynikající)')
    )
    fig = dict(data=[trace2, trace1], layout=layout)
```
'''


graphs = {
    'hist_age': hist_age,
    'alcohol_bar': alcohol_bar,
    'alcohol_box': alcohol_box,
    'alcohol_family': alcohol_family,
    'internet_lifestyle': internet_lifestyle,
    'relationship_age': relationship_age,
    'mother_box': mother_box,
    'mother_hist': mother_hist
}

texts = {
   'hist_age': hist_age_txt,
    'alcohol_bar': alcohol_bar_txt,
    'alcohol_box': alcohol_box_txt,
    'alcohol_family': alcohol_family_txt,
    'internet_lifestyle': internet_lifestyle_txt,
    'relationship_age': relationship_age_txt,
    'mother_box': mother_box_txt,
    'mother_hist': mother_hist_txt
}
