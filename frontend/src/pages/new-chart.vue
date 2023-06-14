<template>

  <div id="app2">
      <div id="minute" ref="minute" ></div>
  </div>

</template>

<script>

import HQChart from 'hqchart'

function DefaultData(){}

DefaultData.GetMinuteOption=function()
{
  var option= 
  {
      Type:'分钟走势图',   //创建图形类型
          
      Windows: //窗口指标
      [
          
      ], 
          
      IsAutoUpdate:true,       //是自动更新数据
      DayCount:1,                 //1 最新交易日数据 >1 多日走势图
      IsShowCorssCursorInfo:true, //是否显示十字光标的刻度信息
      IsShowRightMenu:true,       //是否显示右键菜单
      CorssCursorTouchEnd:true,

      MinuteLine:
      {
          //IsDrawAreaPrice:false,      //是否画价格面积图
      },

      Border: //边框
      {
          Left:1,    //左边间距
          Right:1,   //右边间距
          Top:20,
          Bottom:20
      },
          
      Frame:  //子框架设置
      [
          {SplitCount:3,StringFormat:0},
          {SplitCount:2,StringFormat:0},
          {SplitCount:3,StringFormat:0},
      ],

      ExtendChart:    //扩展图形
      [
          //{Name:'MinuteTooltip' }  //手机端tooltip
      ],
  };

  return option;
}


export default 
{
  data() 
  {
      var data=
      {
          Symbol:'600000.sh',

          Minute:
          {
              JSChart:null,
              Option:DefaultData.GetMinuteOption(),
          }
      };

      return data;

  },

  created()
  {
      
  },

  mounted()
  {
      this.OnSize();

      window.onresize = ()=> { this.OnSize(); }

      this.CreateMinuteChart();
  },
      
  methods:
  {
      OnSize()
      {
          var chartHeight = window.innerHeight-30;
          var chartWidth = window.innerWidth-30;


          var minute=this.$refs.minute;
          minute.style.width=chartWidth+'px';
          minute.style.height=chartHeight+'px';

          if (this.Minute.JSChart) this.Minute.JSChart.OnSize();
      },

      CreateMinuteChart() //创建日线图
      {
          if (this.Minute.JSChart) return;
          this.Minute.Option.Symbol=this.Symbol;
          let chart=HQChart.Chart.JSChart.Init(this.$refs.minute);
          chart.SetOption(this.Minute.Option);
          this.Minute.JSChart=chart;
      },
  }
}
</script>
