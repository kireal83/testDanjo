from django.shortcuts import HttpResponse, redirect, render
from django.forms.models import model_to_dict
# from django.db.models import Q
#        Q是或函数

# from app1.models import Department, UserInfo
#        Department UserIon 是数据库类名

from app1.models import DtsjOld, JbxxXin, GrzhXin, JbxxZl, GrzhZl


# from app1 import models


# from app1 import models
# **重要**视图函数
# Create your views here.

def index(request):
    return HttpResponse("hello world")


def consult(request):
    vbxhm = request.POST.get("bxhm")  # 输入的手册号
    vxm = request.POST.get("xm")  # 输入的姓名
    vsfhm = request.POST.get("sfhm")  # 输入的身份证号码
    xs_name = []
    xs_bxhm = []
    xs_sfhm = []
    # dtsj_old_bxhm = []  # dtsj_old筛选结果中的保险手册号
    dtsj_old_sxjg = None  # dtsj_old数据表中的筛选结果
    jbxx_xin_bxhm = []  # jbxx_xin筛选结果中的保险手册号
    jbxx_xin_sfhm = []  # jbxx_xin筛选结果中的身份证号
    jbxx_xin_sxjg = None  # jbxx_dt数据表中的筛选结果
    grzh_xin_sxjg = []  # grzh_xin数据表中的筛选结果
    jbxx_zl_bxhm = []  # jbxx_zl筛选结果中的保险手册号
    jbxx_zl_sfhm = []  # jbxx_zl筛选结果中的身份证号
    jbxx_zl_sxjg = None  # jbxx_zl数据表中的筛选结果
    grzh_zl_sxjg = []  # grzh_zl数据表中的筛选结果
    jbxx_xin_name = []
    jbxx_zl_name = []

    # 判断输入的是什么
    if vbxhm is not None:
        if len(str.strip(vbxhm)) > 0:
            dtsj_old_sxjg = DtsjOld.objects.filter(bxhm=vbxhm)
            jbxx_xin_sxjg = JbxxXin.objects.filter(bxhm=vbxhm)
            jbxx_zl_sxjg = JbxxZl.objects.filter(bxhm_zl=vbxhm)
    if vxm is not None:
        if len(str.strip(vxm)) > 0:
            dtsj_old_sxjg = DtsjOld.objects.filter(name=vxm)
            jbxx_xin_sxjg = JbxxXin.objects.filter(name=vxm)
            jbxx_zl_sxjg = JbxxZl.objects.filter(name_zl=vxm)

    if vsfhm is not None:
        if len(str.strip(vsfhm)) > 0:
            dtsj_old_sxjg = DtsjOld.objects.filter(bxhm=vsfhm)
            jbxx_xin_sxjg = JbxxXin.objects.filter(sfhm=vsfhm)
            jbxx_zl_sxjg = JbxxZl.objects.filter(sfhm_zl=vsfhm)
    # 判断jbxx_dt数据表是否查询到结果
    if jbxx_xin_sxjg is None:
        return render(request, "consult.html")
    # 使用jbxx_dt数据表中的id匹配grzh_xin数据表中的JBXX_ID
    for item_jbxx_xin in jbxx_xin_sxjg:
        item_grzh_xin = GrzhXin.objects.filter(sfhm_xin=item_jbxx_xin.sfhm).distinct()
        grzh_xin_sxjg.append(item_grzh_xin)
        for i in jbxx_xin_sxjg:  # 去重
            if i.name not in jbxx_xin_name:
                jbxx_xin_name.append(i.name)  # 将所有jbxx_xin_sxjg中的姓名传入jbxx_xin_name中
                xs_name.append(i.name)
        for i in jbxx_xin_sxjg:  # 去重
            if i.bxhm not in jbxx_xin_bxhm:
                jbxx_xin_bxhm.append(i.bxhm)  # 将所有jbxx_xin_sxjg中的保险手册号传入jbxx_xin_bxhm中
                xs_bxhm.append(i.bxhm)
        for i in jbxx_xin_sxjg:  # 去重
            if i.sfhm not in jbxx_xin_sfhm:
                jbxx_xin_sfhm.append(i.sfhm)  # 将所有jbxx_xin_sxjg中的保身份证号传入jbxx_xin_sfhm中
                xs_sfhm.append(i.sfhm)
    # 判断jjbxx_zl数据表是否查询到结果
    if jbxx_zl_sxjg is None:
        return render(request, "consult.html")
    for item_jbxx_zl in jbxx_zl_sxjg:
        item_grzh_zl = GrzhZl.objects.filter(sfhm_grzl=item_jbxx_zl.sfhm_zl).distinct()
        grzh_zl_sxjg.append(item_grzh_zl)
    for i in jbxx_zl_sxjg:  # 去重
        if i.bxhm_zl not in xs_bxhm:
            xs_bxhm.append(i.bxhm_zl)
        if i.bxhm_zl not in jbxx_zl_bxhm:
            jbxx_zl_bxhm.append(i.bxhm_zl)  # 将所有jbxx_zl_sxjg中的保险手册号传入jbxx_zl_bxhm中
    for i in jbxx_zl_sxjg:  # 去重
        if i.sfhm_zl not in xs_sfhm:
            xs_sfhm.append(i.sfhm_zl)
        if i.sfhm_zl not in jbxx_zl_sfhm:
            jbxx_zl_sfhm.append(i.sfhm_zl)  # 将所有jbxx_zl_sxjg中的身份证号传入jbxx_zl_sfhm中
    for i in jbxx_zl_sxjg:  # 去重
        if i.name_zl not in xs_name:
            xs_name.append(i.name_zl)
        if i.name_zl not in jbxx_zl_name:
            jbxx_zl_name.append(i.name_zl)  # 将所有jbxx_zl_sxjg中的姓名传入jbxx_zl_name中
    print(jbxx_zl_name)
    if dtsj_old_sxjg is None:
        dtsj_old_sxjg = DtsjOld.objects.filter(name=xs_name)
    # 将所有dtsj_old_sxjg中的保险手册号传入dtsj_old_bxhm中
    # for item_old_bxhm in dtsj_old_sxjg:
    #     for i in item_old_bxhm:  # 去重
    #         if i not in dtsj_old_bxhm:
    #             dtsj_old_bxhm.append(item_old_bxhm.bxhm)
    return render(request, "consult.html", {
        "xm": vxm,
        "xs_name": xs_name,
        "xs_bxhm": xs_bxhm,
        "xs_sfhm": xs_sfhm,
        "dtsj_old_sxjg": dtsj_old_sxjg,
        "jbxx_xin_name": jbxx_xin_name,
        "grzh_xin_sxjg": grzh_xin_sxjg,
        "jbxx_zl_name": jbxx_zl_name,
        "grzh_zl_sxjg": grzh_zl_sxjg,

    })
