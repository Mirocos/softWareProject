//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    motto: '上传照片',
    userInfo: {}
  },
  //事件处理函数
  uploadImage: function () {
    var that = this
    wx.chooseImage({

      success: function (res) {
        var tempFilePaths = res.tempFilePaths
        wx.getFileSystemManager().readFile({
          filePath: tempFilePaths[0], //选择图片返回的相对路径
          encoding: 'base64', //编码格式
          success: function (resl) {
            var img = resl.data
            console.log(img)
          }
        })
        wx.showToast({
          title: '鉴定中，请稍候',
          icon: 'loading',
          duration: 2000
        })
        wx.request({
          url: 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=0EItXY9pbTxfKRgaFrY5tk2E&client_secret=G3NhYkIDW3CAdiVxNkkwyoDAaIPNhWwY',
          method: 'POST',
          dataType: "json",
          header: {
            'content-type': 'application/json;charset=UTF-8'
          },
          success: function (res1) {
            var token = res1.data
            wx.uploadFile({
              url: 'https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=' + token.access_token, //仅为示例，非真实的接口地址
              header: {
                'content-type': 'application/json'
              },
              filePath: tempFilePaths[0],
              name: 'file',
              success: function (res2) {
                console.log(res2.data)
                wx.hideToast()
                var data = JSON.parse(res2.data)
                if (!data.attributes) {
                  that.setData({
                    userInfo: {
                      avatarUrl: data.url,
                      tips: '未检测到人脸'
                    }
                  })
                  return
                }
                const genders = {
                  'Male': '帅哥',
                  'Female': '美女'
                }
                that.setData({
                  userInfo: {
                    avatarUrl: data.url,
                    tips: '一位' + data.attributes.age.value + '岁的' + genders[data.attributes.gender.value]
                  }
                })
                //do something
              }
            })
          }
        })
      }
    })
  },
  onLoad: function () {
    console.log('onLoad')
  }
})
