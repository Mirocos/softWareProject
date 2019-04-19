// pages/baike/baike.js
Page({
  data: {
    indexmenu: [],
    imgUrls: []
  },
  onLoad: function () {
    //生命周期函数--监听页面加载
    this.fetchData();
    // var that = this
    // //调用应用实例的方法获取全局数据
    // app.getUserInfo(function(userInfo){
    //   //更新数据
    //   that.setData({
    //     userInfo:userInfo
    //   })
    // })
  },
  fetchData: function () {
    this.setData({
      indexmenu: [
        {
          'icon': './../../images/23.png',
          'text': '新手养宠',
          'url': '1'
        },
        {
          'icon': './../../images/24.png',
          'text': '宠物饮食',
          'url': '2'
        },
        {
          'icon': './../../images/3.png',
          'text': '宠物护理',
          'url': '3'
        },
        {
          'icon': './../../images/animalNine.png',
          'text': '常见疾病',
          'url': '4'
        },
        {
          'icon': './../../images/book.png',
          'text': '宠物训练',
          'url': '/5'
        },
        {
          'icon': './../../images/timg.jpg',
          'text': '宠物品种',
          'url': '6'
        },
      ],
      imgUrls: [
        '../../images/cat.jpg',
        '../../images/cat1.jpg',
        '../../images/t.jpg'
      ]
    })
  },

  onReady: function () {
    //生命周期函数--监听页面初次渲染完成
    // console.log('onReady');
  },
  onShow: function () {
    //生命周期函数--监听页面显示
    // console.log('onShow');
  },
  onHide: function () {
    //生命周期函数--监听页面隐藏
    // console.log('onHide');
  },
  onUnload: function () {
    //生命周期函数--监听页面卸载
    // console.log('onUnload');
  },
  onPullDownRefresh: function () {
    //页面相关事件处理函数--监听用户下拉动作
    // console.log('onPullDownRefresh');
  },
  onReachBottom: function () {
    //页面上拉触底事件的处理函数
    // console.log('onReachBottom');
  }
})