//index.js
//获取应用实例
var app = getApp()
Page({
  data: {
    motto: '上传照片',
    userInfo: {},
    img_arr: [],
    formdata: '',
  },
  //事件处理函数
  uploadImage: function () {
    var that = this
    wx.chooseImage({

      success: function (res) {
        var tempFilePaths = res.tempFilePaths
        wx.showToast({
          title: '鉴定中，请稍候',
          icon: 'loading',
          duration: 2000
        })
        wx.request({
          url: 'http://127.0.0.1:8000/Animal/', //仅为示例，非真实的接口地址
          header: {
              'content-type': 'application/json'
          },
          success: function (res2) {
            console.log(res2.data)

                //do something
          }
        })
      }
    })
  },
  formSubmit: function (e) {
    var id = e.target.id
    var adds = e.detail.value;
    adds.program_id = app.jtappid
    adds.openid = app._openid
    adds.zx_info_id = this.data.zx_info_id
    this.upload()
  },

  upload: function () {
    var that = this
    for (var i = 0; i < this.data.img_arr.length; i++) {
      wx.uploadFile({
        url: 'http://127.0.0.1:8000/Animal',
        filePath: that.data.img_arr[i],
        name: 'content',
        formData: this.adds,
        success: function (res) {
          console.log(res)
          if (res) {
            wx.showToast({
              title: '已提交发布！',
              duration: 3000
            });
          }
        }
      })
    }
    this.setData({
      formdata: ''
    })
  },
  upimg: function () {
    var that = this;
    if (this.data.img_arr.length < 3) {
      wx.chooseImage({
        sizeType: ['original', 'compressed'],
        success: function (res) {
          that.setData({
            img_arr: that.data.img_arr.concat(res.tempFilePaths)
          })
        }
      })
    } else {
      wx.showToast({
        title: '最多上传三张图片',
        icon: 'loading',
        duration: 3000
      });
    }
  },

  onLoad: function () {
    console.log('onLoad')
  }
})
