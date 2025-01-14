# -*- coding: utf-8 -*-

from .type import WeChatPayType


class WeChatPay():
    def __init__(self,
                 wechatpay_type,
                 mchid,
                 parivate_key,
                 cert_serial_no,
                 appid,
                 apiv3_key,
                 notify_url=None,
                 cert_dir=None):
        """
        :param wechatpay_type: 微信支付类型，示例值：WeChatPayType.MINIPROG
        :param mchid: 直连商户号，示例值：'1230000109'
        :param mch_private_key: 商户证书私钥，示例值：'MIIEvwIBADANBgkqhkiG9w0BAQE...'
        :param mch_key_serial_no: 商户证书序列号，示例值：'444F4864EA9B34415...'
        :param appid: 应用ID，示例值：'wxd678efh567hg6787'
        :param mch_apiv3_key: 商户APIv3密钥，示例值：'a12d3924fd499edac8a5efc...'
        :param notify_url: 通知地址，示例值：'https://www.weixin.qq.com/wxpay/pay.php'
        :param cert_dir: 平台证书存放目录，示例值：'/server/cert'
        """
        from .core import Core

        self._type = wechatpay_type
        self._mchid = mchid
        self._appid = appid
        self._notify_url = notify_url
        self._core = Core(mchid=self._mchid,
                          cert_serial_no=cert_serial_no,
                          private_key=parivate_key,
                          apiv3_key=apiv3_key,
                          cert_dir=cert_dir)

    def sign(self, data):
        """计算签名值paySign，供JSAPI、APP、NATIVE调起支付时使用
        :param data: 需要签名的参数清单，示例值：['wx888','1414561699','5K8264ILTKCH16CQ2502S....','prepay_id=wx201410272009395522657....']
        """
        sign_str = '\n'.join(data) + '\n'
        return self._core.sign(sign_str)

    def decrypt_callback(self, headers, body):
        """解密回调接口收到的信息
        """
        return self._core.decrypt_callback(headers, body)

    from .businesscircle import points_notify, user_authorization
    from .transaction import (close, combine_close, combine_pay, combine_query,
                              download_bill, fundflow_bill, pay, query,
                              query_refund, refund, trade_bill)
