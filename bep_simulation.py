
# simulating company BEP through interactive cost/revenue plot (spent 2-3 hours making it with limited matplotlib knowledge at the time (Summer 2019))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib as mpl
import matplotlib.font_manager as fm

#visiblee = input("Ax2 Visible? (True or False): ")
month = int(input("How many months passed?: "))

##setting Korean fonts
font_location = '/Users/jinhongkim/Library/Fonts/KakaoRegular.ttf'
font_name = fm.FontProperties(fname = font_location).get_name()
mpl.rc('font', family = font_name)

##create plots
fig, (ax1, ax2) = plt.subplots(1,2,sharex=True)
ax1.set_position([0.55,0.1,0.33,0.6]) #left, bottom, width, height
ax2.set_position([0.1,0.1,0.33,0.45])
ax2.set_yscale("log")

x = np.arange(0.0, 7.0, 0.01)

##default values
#a = 18.37
#b = 1.38
c = 10.24
d = 2.47
inc = 0.01
q = 0.2

##user input for costs
i_1 = float(input("초기 총 지출 비용: "))
i_2 = float(input("20년 1월 지출 비용: "))
i_3 = float(input("20년 2월 지출 비용: "))
i_4 = float(input("20년 3월 지출 비용: "))
i_5 = float(input("20년 4월 지출 비용 "))

##people graph -- default multipliers
axx = 400
bxx = 30000
cxx = 37000
dxx = 53000
exx = 200000
fxx = 266666

##money graph -- cost getting trendline equation
xxx = np.arange(0, 5*(1/12), 1/12)
yyy = np.array([i_1, np.sum([i_1,i_2]), np.sum([i_1,i_2,i_3]),np.sum([i_1,i_2,i_3,i_4]), np.sum([i_1,i_2,i_3,i_4,i_5])])
zzzz = np.polyfit(xxx, yyy, 2)
zzz = np.poly1d(zzzz)
xp = np.linspace(0, 4, 100)

##money graph -- equations for the two lines
p = c * np.power(x,d)
s = zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0]

##money graph -- plot the above two equations
l, = ax1.plot(x, s, lw=2, color='red', label='비용')
j, = ax1.plot(x, p, lw=2, color='blue', label='매출')

##getting the bep point
idx = np.argwhere(np.diff(np.sign(s - p))).flatten()
xv = idx[0]/100

##getting the bep lines
k = ax1.axvline(xv,ymin=0, ymax=1, linestyle='--')
k2 = ax2.axvline(xv,ymin=0, ymax=1, linestyle='--')
u = ax1.axhline(c*np.power(xv,d),xmin=0,xmax=1, linestyle='--')

##annotating the bep point
z = ax1.annotate('BEP: 출시 {}년 최소 {:.2f}억원'.format(xv,zzz[2]*np.power(xv,2)+zzz[1]*xv+zzz[0]), xy=(xv, zzz[2]*np.power(xv,2)+zzz[1]*xv+zzz[0]), xytext=(xv+q, zzz[2]*np.power(xv,2)+zzz[1]*xv+zzz[0]+10*q))

##axes and legend labels
ax1.axis([0, 4, 0, 100])
ax1.set_xlabel('출시 이후 시간 (년)')
ax1.set_ylabel('돈 (억원)')
ax1.legend(loc='upper left')

dep_l = (zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*axx
aaa, = ax2.plot(x,dep_l,lw=2,color='purple', label='최소 입금자')

reg_l = (zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*bxx
bbb, = ax2.plot(x,reg_l,lw=2,color='blue', label='최소 가입자')

vis_l = (zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*cxx
ccc, = ax2.plot(x,vis_l,lw=2,color='green', label='최소 방문자')

clk_l = (zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*dxx
ddd, = ax2.plot(x,clk_l,lw=2,color='yellow', label='최소 클릭자')

ads_l = (zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*exx
eee, = ax2.plot(x,ads_l,lw=2,color='orange', label='최소 광고노출자')

pot_l = (zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*fxx
fff, = ax2.plot(x,pot_l,lw=2,color='grey', label='최소 잠재고객')

lg_1 = 0.01
lg_2 = 1.35
ax2.axis([0, 4, 0, 100000000])
ax2.set(xlabel='출시 이후 시간 (년)', ylabel='유저 (명)')
ax2.legend(loc='upper left', bbox_to_anchor=(lg_1, lg_2))


##sliders
sld_color = 'white' #left, bottom, width, height
#a_slider = plt.axes([0.62, 0.95, 0.3, 0.03], facecolor=sld_color)
#b_slider = plt.axes([0.62, 0.90, 0.3, 0.03], facecolor=sld_color)
c_slider = plt.axes([0.62, 0.85, 0.3, 0.03], facecolor=sld_color)
d_slider = plt.axes([0.62, 0.80, 0.3, 0.03], facecolor=sld_color)

haha = 0.95
visiblee = True
aa_slider = plt.axes([0.12, haha,0.25, 0.03], facecolor=sld_color, visible=visiblee)
bb_slider = plt.axes([0.12, haha-0.04, 0.25, 0.03], facecolor=sld_color, visible=visiblee)
cc_slider = plt.axes([0.12, haha-0.08, 0.25, 0.03], facecolor=sld_color, visible=visiblee)
dd_slider = plt.axes([0.12, haha-0.12, 0.25, 0.03], facecolor=sld_color, visible=visiblee)
ee_slider = plt.axes([0.12, haha-0.16, 0.25, 0.03], facecolor=sld_color, visible=visiblee)
ff_slider = plt.axes([0.12, haha-0.20, 0.25, 0.03], facecolor=sld_color, visible=visiblee)

#a_sld = Slider(a_slider, '비용 Curve', 0, 20.0, valinit=a,valstep=inc)
#b_sld = Slider(b_slider, '비용 Slope', 0, 7.0, valinit=b, valstep=inc)
c_sld = Slider(c_slider, '매출 Curve', 0, 20.0, valinit=c,valstep=inc)
d_sld = Slider(d_slider, '매출 Slope', 0, 7.0, valinit=d, valstep=inc)

aa_sld = Slider(aa_slider, '입금자 배수', axx*0.8, axx*1.2, valinit=axx,valstep=inc)
bb_sld = Slider(bb_slider, '가입자 배수', axx*1.2, bxx*1.2, valinit=bxx, valstep=inc)
cc_sld = Slider(cc_slider, '방문자 배수', bxx*1.2, cxx*1.2, valinit=cxx,valstep=inc)
dd_sld = Slider(dd_slider, '클릭자 배수', cxx*1.2, dxx*1.2, valinit=dxx, valstep=inc)
ee_sld = Slider(ee_slider, '광고노출자 배수', dxx*1.2, exx*1.2, valinit=exx,valstep=inc)
ff_sld = Slider(ff_slider, '잠재고객 배수', exx*1.2, fxx*1.2, valinit=fxx, valstep=inc)



def update(val):
    #aa = a_sld.val
    #bb = b_sld.val
    cc = c_sld.val
    dd = d_sld.val
    ii = np.argwhere(np.diff(np.sign(s - cc*(x)**dd))).flatten()

    #s = zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0]
    #idx = np.argwhere(np.diff(np.sign(s - p))).flatten()
    #xv = idx[0]/100

    axxx = aa_sld.val
    bxxx = bb_sld.val
    cxxx = cc_sld.val
    dxxx = dd_sld.val
    exxx = ee_sld.val
    fxxx = ff_sld.val
    l.set_ydata(s)
    j.set_ydata(cc*(x)**dd)
    k.set_xdata(ii[0]/100)
    u.set_ydata(cc*np.power(ii[0]/100,dd))
    k2.set_xdata(ii[0]/100)

    #sz_5 = zzz[2]*np.power((2/12),2) + zzz[1]*(2/12) + zzz[0]
    sz_5 = cc * np.power(month/12,dd)
    #sz_5 = (zzz[2]*np.power((2/12),2)+zzz[1]*(2/12)+zzz[0])
    sz = zzz[2]*np.power(ii[0]/100,2) + zzz[1]*ii[0]/100 + zzz[0]
    #print(sz_5)
    #print(s)

    aaa.set_label('최소 입금자 [BEP때] {:.0f}명 / [{}번째 달] {:.0f}명'.format(sz*axxx,month,sz_5*axxx))
    bbb.set_label('최소 가입자 [BEP때] {:.0f}명 / [{}번째 달] {:.0f}명'.format(sz*bxxx,month,sz_5*bxxx))
    ccc.set_label('최소 방문자 [BEP때] {:.0f}명 / [{}번째 달] {:.0f}명'.format(sz*cxxx,month,sz_5*cxxx))
    ddd.set_label('최소 클릭자 [BEP때] {:.0f}명 / [{}번째 달] {:.0f}명'.format(sz*dxxx,month,sz_5*dxxx))
    eee.set_label('최소 광고 노출자 [BEP때] {:.0f}명 / [{}번째 달] {:.0f}명'.format(sz*exxx,month,sz_5*exxx))
    fff.set_label('최소 잠재 고객 [BEP때] {:.0f}명 / [{}번째 달] {:.0f}명'.format(sz*fxxx,month,sz_5*fxxx))
    aaa.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*axxx)
    bbb.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*bxxx)
    ccc.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*cxxx)
    ddd.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*dxxx)
    eee.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*exxx)
    fff.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*fxxx)

    z.set_text('BEP: 출시 {}년 최소 {:.2f}억원'.format(ii[0]/100, (zzz[2]*np.power((ii[0]/100),2)+zzz[1]*(ii[0]/100)+zzz[0])))
    z.set_position((ii[0]/100+q, (zzz[2]*np.power((ii[0]/100),2)+zzz[1]*(ii[0]/100)+zzz[0])+10*q))
    ax2.legend(loc='upper left', bbox_to_anchor=(lg_1, lg_2))
    ax2.set_yscale("log")
    fig.canvas.draw_idle()


#a_sld.on_changed(update)
#b_sld.on_changed(update)
c_sld.on_changed(update)
d_sld.on_changed(update)

aa_sld.on_changed(update)
bb_sld.on_changed(update)
cc_sld.on_changed(update)
dd_sld.on_changed(update)
ee_sld.on_changed(update)
ff_sld.on_changed(update)


resetax = plt.axes([0.87, 0.73, 0.1, 0.04])
button = Button(resetax, 'Reset', color=sld_color, hovercolor='0.975')

def reset(event):
    #a_sld.reset()
    #b_sld.reset()
    c_sld.reset()
    d_sld.reset()
    aa_sld.reset()
    bb_sld.reset()
    cc_sld.reset()
    dd_sld.reset()
    ee_sld.reset()
    ff_sld.reset()
button.on_clicked(reset)

saveax = plt.axes([0.87, 0.02, 0.1, 0.04])
s_button = Button(saveax, 'Save', color=sld_color, hovercolor='0.975')

def save(event):
    f = open('예시 BEP.csv', 'w')
    cc = c_sld.val
    dd = d_sld.val
    ii = np.argwhere(np.diff(np.sign(s - cc*(x)**dd))).flatten()

    #s = zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0]
    #idx = np.argwhere(np.diff(np.sign(s - p))).flatten()
    #xv = idx[0]/100

    axxx = aa_sld.val
    bxxx = bb_sld.val
    cxxx = cc_sld.val
    dxxx = dd_sld.val
    exxx = ee_sld.val
    fxxx = ff_sld.val
    l.set_ydata(s)
    j.set_ydata(cc*(x)**dd)
    k.set_xdata(ii[0]/100)
    u.set_ydata(cc*np.power(ii[0]/100,dd))
    k2.set_xdata(ii[0]/100)

    #sz_5 = zzz[2]*np.power((2/12),2) + zzz[1]*(2/12) + zzz[0]
    sz_5 = cc * np.power(month/12,dd)
    #sz_5 = (zzz[2]*np.power((2/12),2)+zzz[1]*(2/12)+zzz[0])
    sz = zzz[2]*np.power(ii[0]/100,2) + zzz[1]*ii[0]/100 + zzz[0]
    #print(sz_5)
    #print(s)

    aaa.set_label('최소 입금자 [BEP때] {:.0f} / [{}번째 달] {:.0f}'.format(sz*axxx,month,sz_5*axxx))
    bbb.set_label('최소 가입자 [BEP때] {:.0f} / [{}번째 달] {:.0f}'.format(sz*bxxx,month,sz_5*bxxx))
    ccc.set_label('최소 방문자 [BEP때] {:.0f} / [{}번째 달] {:.0f}'.format(sz*cxxx,month,sz_5*cxxx))
    ddd.set_label('최소 클릭자 [BEP때] {:.0f} / [{}번째 달] {:.0f}'.format(sz*dxxx,month,sz_5*dxxx))
    eee.set_label('최소 광고 노출자 [BEP때] {:.0f} / [{}번째 달] {:.0f}'.format(sz*exxx,month,sz_5*exxx))
    fff.set_label('최소 잠재 고객 [BEP때] {:.0f} / [{}번째 달] {:.0f}'.format(sz*fxxx,month,sz_5*fxxx))
    aaa.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*axxx)
    bbb.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*bxxx)
    ccc.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*cxxx)
    ddd.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*dxxx)
    eee.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*exxx)
    fff.set_ydata((zzz[2]*np.power(x,2)+zzz[1]*x+zzz[0])*fxxx)

    z.set_text('BEP: 출시 {}년 최소 목표 {:.2f}억원'.format(ii[0]/100, (zzz[2]*np.power((ii[0]/100),2)+zzz[1]*(ii[0]/100)+zzz[0])))
    z.set_position((ii[0]/100+q, (zzz[2]*np.power((ii[0]/100),2)+zzz[1]*(ii[0]/100)+zzz[0])+10*q))
    ax2.legend(loc='upper left', bbox_to_anchor=(lg_1, lg_2))
    ax2.set_yscale("log")

    #string_v = '최소 입금자 [BEP때] {:.2f} / [{}번째 달] {:.2f}'.format(sz*axxx,month,sz_5*axxx)+','+'최소 가입자 [BEP때] {:.2f} / [{}번째 달] {:.2f}'.format(sz*bxxx,month,sz_5*bxxx)+','+'최소 방문자 [BEP때] {:.2f} / [{}번째 달] {:.2f}'.format(sz*cxxx,month,sz_5*cxxx)+','+'최소 클릭자 [BEP때] {:.2f} / [{}번째 달] {:.2f}'.format(sz*dxxx,month,sz_5*dxxx)+','+'최소 광고 노출자 [BEP때] {:.2f} / [{}번째 달] {:.2f}'.format(sz*exxx,month,sz_5*exxx)+','+'최소 잠재 고객 [BEP때] {:.2f} / [{}번째 달] {:.2f}'.format(sz*fxxx,month,sz_5*fxxx)

    string_vv = '최소 입금자'+','+'{:.0f}명'.format(sz*axx)+'\n'+'최소 가입자'+','+'{:.0f}명'.format(sz*bxx)+'\n'+'최소 방문자'+','+'{:.0f}명'.format(sz*cxx)+'\n'+'최소 클릭자'+','+'{:.0f}명'.format(sz*dxx)+'\n'+'최소 광고 노출자'+','+'{:.0f}명'.format(sz*exx)+'\n'+'최소 잠재고객'+','+'{:.0f}명'.format(sz*fxx)+'\n'
    f.write('BEP (누적)'+'\n'+'출시'+','+'{}년'.format(ii[0]/100)+'\n'+'최소'+','+'{:.2f}억원'.format(zzz[2]*np.power((ii[0]/100),2)+zzz[1]*(ii[0]/100)+zzz[0])+'\n'+'\n'+str(string_vv))
    f.write('\n'+'20년 {}월 최소 입금자'.format(month)+','+'{:.0f}명'.format(sz_5*axxx)+'\n'+'20년 {}월 최소 가입자'.format(month)+','+'{:.0f}명'.format(sz_5*bxxx)+'\n'+'20년 {}월 최소 방문자'.format(month)+','+'{:.0f}명'.format(sz_5*cxxx)+'\n'+'20년 {}월 최소 클릭자'.format(month)+','+'{:.0f}명'.format(sz_5*dxxx)+'\n'+'20년 {}월 최소 광고 노출자'.format(month)+','+'{:.0f}명'.format(sz_5*exxx)+'\n'+'20년 {}월 최소 잠재고객'.format(month)+','+'{:.0f}명'.format(sz_5*fxxx))
    f.close()
s_button.on_clicked(save)

ax2.set_visible(True)

plt.show()
