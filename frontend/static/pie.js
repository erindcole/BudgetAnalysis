function draw_pie(pie_data){


  var data = {};
  var cat = [];
  pie_data.forEach(function(e) {

      if (!(e.name in cat)){
        cat.push(e.name);
      }
      if (e.name in data) {
        data[e.name] += e.amount;
      } else {
        data[e.name] = e.amount;
      }
  }); 

  console.log(data);
  console.log(cat);

  var chart = c3.generate({
        bindto: '#chart_pie',
        data: {
          json: [ data ],
          keys: {
            value: cat,
          },
          type: 'pie'
        }
  });

}
