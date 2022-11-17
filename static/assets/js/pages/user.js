// const config = {
//   type: 'line',
//   data: data,
// };

// const labels = Utils.months({count: 7});
// const data = {
//   labels: labels,
//   datasets: [{
//     label: 'New user',
//     data: [65, 59, 80, 81, 56, 55, 40],
//     fill: false,
//     borderColor: 'rgb(75, 192, 192)',
//     tension: 0.1
//   }]
// };

// var data = [
//       { y: '2014', a: 50, b: 90},
//       { y: '2015', a: 65,  b: 75},
//       { y: '2016', a: 50,  b: 50},
//       { y: '2017', a: 75,  b: 60},
//       { y: '2018', a: 80,  b: 65},
//       { y: '2019', a: 90,  b: 70},
//       { y: '2020', a: 100, b: 75},
//       { y: '2021', a: 115, b: 75},
//       { y: '2022', a: 120, b: 85},
//       { y: '2023', a: 145, b: 85},
//       { y: '2024', a: 160, b: 95}
//     ],
//     config = {
//       data: data,
//       xkey: 'y',
//       ykeys: ['a', 'b'],
//       labels: ['Total Income', 'Total Outcome'],
//       fillOpacity: 0.6,
//       hideHover: 'auto',
//       behaveLikeLine: true,
//       resize: true,
//       pointFillColors:['#ffffff'],
//       pointStrokeColors: ['black'],
//       lineColors:['gray','red']
//   };
// config.element = 'new-user-day-occu';
// Morris.Line(config);
// config.element = 'line-chart-2';
// Morris.Line(config);
// config.element = 'bar-chart';
// Morris.Bar(config);
// config.element = 'stacked';
// config.stacked = true;
// Morris.Bar(config);
// Morris.Donut({
//   element: 'pie-chart',
//   data: [
//     {label: "Friends", value: 30},
//     {label: "Allies", value: 15},
//     {label: "Enemies", value: 45},
//     {label: "Neutral", value: 10}
//   ]
// });


// const products = [];
// import {user_by_date} from '/templates/home/user.html';
// import { python } from "pythonia";
// var user_by_date = {{config.db['user_by_date']}};
// 'use strict';

// function load_data(new_data) {
//     elem = new_data;
// }

// const data = [];
// for (let i = 0; i < user.length; i++) {
//   data[data.length] = {y:user[i]['id'], a: };
// }

// $(document).ready(function() {
//     setTimeout(function() {
//     // import {user_by_date} from '/templates/home/user.html';
//         // const products = [];
//     // const user_by_date = require('../../../../templates/home/user.html')
//     // var elem = config.db['user_by_date'];

//     // [ line-angle-chart ] Start
//     // Morris.Line({
//     //     element: 'new-user-day-occu',
        
//     //     // data: user_by_date,
//     //     // xkey: 'date',
//     //     // redraw: true,
//     //     // resize: true,
//     //     // smooth: false,
//     //     // ykeys: ['user'],
        
        
//     //     data: [{
//     //             y: '2006',
//     //             a: 100,
//     //             b: 90
//     //         },
//     //         {
//     //             y: '2007',
//     //             a: 75,
//     //             b: 65
//     //         },
//     //         {
//     //             y: '2008',
//     //             a: 50,
//     //             b: 40
//     //         },
//     //         {
//     //             y: '2009',
//     //             a: 75,
//     //             b: 65
//     //         },
//     //         {
//     //             y: '2010',
//     //             a: 50,
//     //             b: 40
//     //         },
//     //         {
//     //             y: '2011',
//     //             a: 75,
//     //             b: 65
//     //         },
//     //         {
//     //             y: '2012',
//     //             a: 100,
//     //             b: 90
//     //         }
//     //     ],
        

//     //     xkey: 'y',
//     //     redraw: true,
//     //     resize: true,
//     //     smooth: false,
//     //     ykeys: ['a'],

//     //     hideHover: 'auto',
//     //     responsive:true,
//     //     labels: ['users'],
//     //     lineColors: ['#1de9b6', '#04a9f5']
//     // });
//     // [ line-angle-chart ] end

//     // [ line-smooth-chart ] start
//     Morris.Line({
//         element: 'line-chart-2',
//         data: [{
//                 y: '2006',
//                 a: 100,
//                 b: 90
//             },
//             {
//                 y: '2007',
//                 a: 75,
//                 b: 65
//             },
//             {
//                 y: '2008',
//                 a: 50,
//                 b: 40
//             },
//             {
//                 y: '2009',
//                 a: 75,
//                 b: 65
//             },
//             {
//                 y: '2010',
//                 a: 50,
//                 b: 40
//             },
//             {
//                 y: '2011',
//                 a: 75,
//                 b: 65
//             },
//             {
//                 y: '2012',
//                 a: 100,
//                 b: 90
//             }
//         ],
//         xkey: 'y',
//         redraw: true,
//         resize: true,
//         smooth: false,
//         ykeys: ['a', 'b'],
//         hideHover: 'auto',
//         responsive:true,
//         labels: ['Series A', 'Series B'],
//         lineColors: ['#1de9b6', '#A389D4']
//     });

//     var graph = Morris.Donut({
//         element: 'donut-chart-occu',
//         data: [{
//                 value: 60,
//                 label: 'Data 1'
//             },
//             {
//                 value: 20,
//                 label: 'Data 1'
//             },
//             {
//                 value: 10,
//                 label: 'Data 1'
//             },
//             {
//                 value: 5,
//                 label: 'Data 1'
//             }
//         ],
//         colors: [
//             '#1de9b6',
//             '#A389D4',
//             '#04a9f5',
//             '#1dc4e9',
//         ],
//         resize: true,
//         formatter: function(x) {
//             return "val : " + x
//         }
//     }); 

//     var graph = Morris.Donut({
//         element: 'donut-chart-age',
//         data: [{
//                 value: 60,
//                 label: 'Data 1'
//             },
//             {
//                 value: 20,
//                 label: 'Data 1'
//             },
//             {
//                 value: 10,
//                 label: 'Data 1'
//             },
//             {
//                 value: 5,
//                 label: 'Data 1'
//             }
//         ],
//         colors: [
//             '#1de9b6',
//             '#A389D4',
//             '#04a9f5',
//             '#1dc4e9',
//         ],
//         resize: true,
//         formatter: function(x) {
//             return "val : " + x
//         }
//     });    
    
//         }, 700);
// });
