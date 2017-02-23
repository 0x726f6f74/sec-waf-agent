/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50534
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50534
File Encoding         : 65001

Date: 2017-02-03 15:56:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for waf_configure
-- waf配置选项
-- ----------------------------
DROP TABLE IF EXISTS `waf_configure`;
CREATE TABLE `waf_configure` (
  `config_waf_enable` int(1) NOT NULL,
  `config_white_url_check` int(1) NOT NULL,
  `config_white_ip_check` int(1) NOT NULL,
  `config_black_ip_check` int(1) NOT NULL,
  `config_url_check` int(1) NOT NULL,
  `config_url_args_check` int(1) NOT NULL,
  `config_user_agent_check` int(1) NOT NULL,
  `config_cookie_check` int(1) NOT NULL,
  `config_cc_check` int(1) NOT NULL,
  `config_cc_rate` text NOT NULL,
  `config_post_check` int(1) NOT NULL,
  `config_waf_output` int(1) NOT NULL,    #存在两个值html,redirect  代表重定向自定义错误页面和重定向错误链接页面
  `config_waf_redirect_url` text NOT NULL,  
  `config_output_html` text NOT NULL, 
  `config_update_status` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of waf_configure
-- ----------------------------
INSERT INTO `waf_configure` VALUES ('1', '1', '1', '1', '1', '1', '1', '1', '1', '100/5', '1', '1', '1drfdfsd', '1', '0');

-- ----------------------------
-- Table structure for waf_rule
-- 添加规则表
-- ----------------------------
DROP TABLE IF EXISTS `waf_rule`;
CREATE TABLE `waf_rule` (
  `rule_id` text NOT NULL,
  `rule_title` varchar(80) NOT NULL,
  `rule_type` int(1) NOT NULL,      #存在多个选项1-8;args,blackip,cookie,post,url,useragent,whiteip,whiteurl
  `rule_match` text NOT NULL,     #多个规则以,分隔
  `rule_update_status` int(1) NOT NULL        #有两个值0,1 ；1代表及时更新；0代表定时更新
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of waf_rule
-- ----------------------------
INSERT INTO `waf_rule` VALUES ('Waf-Rule-20170203', '文件包含', '1', '\\.\\.\\/', '0');
