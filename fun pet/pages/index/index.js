//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    headimg :[
      {url: '/images/cat.jpg'},
      {url:'/images/cat1.jpg'},
      {url:'/images/t.jpg'},
    ],
    indexmenu:[],
  },
  //事件处理函数
  onLoad: function () {
    this.fetchData();
  },
  fetchData:function(){
    this.setData({
      indexmenu: [
        {
          'icon': './../../images/more1.png',
          'text': '宠物百科',
          'url': 'baike'
        },
        {
          'icon': './../../images/more2.png',
          'text': '宠物识别',
          'url': 'race'
        },
        {
          'icon': './../../images/more3.png',
          'text': '颜值评定',
          'url': 'face'
        }
      ],
  })
},
  changeRoute: function (url) {
    wx.navigateTo({
      url: `../${url}/${url}`
    })
  },
})

