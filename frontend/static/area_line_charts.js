function draw_area_line_chart(x, income, expense){

    var chart = c3.generate({
        bindto: '#chart',
        data: {
          x: 'x',
          xFormat: '%m/%d/%Y',
          columns: [
            ['x'].concat(x.x),
            ['income'].concat(income['income']),
            ['expense'].concat(expense['expense']),
          ],
          colors: {
            income: '#6EEAD7',
            expense: '#FF5B5E',
          },
          types: {
            income: 'area-spline',
            expense: 'area-spline',
          }
        },
        subchart: {
          size: {
              height: 40
          },
          show: true
        },
        zoom: {
            enabled: true
        },
        axis: {

            x: {
                type: 'timeseries',
                tick: {
                    format: '%Y-%m-%d',
                    //values: ['01/01/2018', '02/01/2018', '03/01/2018'],
                    fit: true,
                    rotate: 75
                }
            },

            y: {

                tick: {

                    format: d3.format("$,")

                }
            }
        }
    });

    chart.resize({height:600, width:1200});
};
