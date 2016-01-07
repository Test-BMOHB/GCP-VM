#Developer    : Ivana Donevska
#Date         : 2015-12-10
#Program Name : Credit Card Transactions Scenario - Overpayment
#Version#     :1
#Description  : Code that generates credit card transactions and scenarios
#-----------------------------------------------------------------------------
# History  | ddmmyyyy  |  User     |                Changes       
#          | 11122015  | Ivana D.  | Intial Coding Steps 
#          | 12232015  | Ivana D.  | Added date for refund to be +90 days of                                                                            
#-----------------------------------------------------------------------------*/

import python_account_ID
from random import randrange
from random import random
import random
from datetime import datetime
from random import shuffle
from faker import Faker
from barnum import gen_data
import csv
from datetime import date, timedelta
fake = Faker()

#Steps 1-4
#1)Define list with Merchant Category Codes
#2)Define list with Transaction Types based on how often a transaction should appear
#3)Define Country_Green Codes list
#4)Define a dictionary with all merchants

#Tran Type Percentage Distribution Table:
#Transaction Type	Green	Yellow	Red
#Cash Advance	        5	15      20
#Cash Payment			5	10	    20
#Purchase				55	37	    20
#Payment				20	10	    5
#Payment Reversal		1	5	    0
#Wire Transfer			3	0	    10
#Void					3	10	    0
#Refund					3	10	    15
#ACH 					5	3	    10
#						100	100	    100

Transaction_Type_Credits = ['Cash Payment','Payment','Payment Reversal','Wire Transfer']
Transaction_Type_Debits = ['Cash Advance','Purchase']

Country_Yellow = ['BH', 'BB', 'BW', 'BG', 'CM', 'CG', 'HR', 'CW', 'CZ', 'TL', 'TP', 'SV', 'ET', 'GE', 'IN', 'IL', 'JM', 'KI', 'XK', 'LS', 'MK', 'MT', 'FM', 'ME', 'NA', 'NR', 'NZ', 'NU', 'PS', 'PL', 'QA', 'RW', 'RS', 'SG', 'SK', 'ZA', 'ES', 'TW', 'TC', 'AE']
Merchant_Category_Yellow = ['4215', '4722', '5099', '5122', '5131', '5541', '5542', '5921', '5932', '6011', '6012', '6051', '6211', '7210', '7216', '7531', '7535', '7538', '7542', '7631', '8398']
Transaction_Type_Yellow = ['ACH', 'ACH', 'ACH', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Advance', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Cash Payment', 'Payment Reversal', 'Payment Reversal', 'Payment Reversal', 'Payment Reversal', 'Payment Reversal', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund', 'Void', 'Refund']

Merchant_Category_Green = ['742', '763', '780', '1520', '1711', '1731', '1740', '1750', '1761', '1771', '1799', '2741', '2791', '2842', '3000', '3001', '3002', '3003', '3004', '3005', '3006', '3007', '3008', '3009', '3010', '3011', '3012', '3013', '3014', '3015', '3016', '3017', '3018', '3019', '3020', '3021', '3022', '3023', '3024', '3025', '3026', '3027', '3028', '3029', '3030', '3031', '3032', '3033', '3034', '3035', '3036', '3037', '3038', '3039', '3040', '3041', '3042', '3043', '3044', '3045', '3046', '3047', '3048', '3049', '3050', '3051', '3052', '3053', '3054', '3055', '3056', '3057', '3058', '3059', '3060', '3061', '3062', '3063', '3064', '3065', '3066', '3067', '3068', '3069', '3070', '3071', '3072', '3073', '3074', '3075', '3076', '3077', '3078', '3079', '3080', '3081', '3082', '3083', '3084', '3085', '3086', '3087', '3088', '3089', '3090', '3091', '3092', '3093', '3094', '3095', '3096', '3097', '3098', '3099', '3100', '3101', '3102', '3103', '3104', '3105', '3106', '3107', '3108', '3109', '3110', '3111', '3112', '3113', '3114', '3115', '3116', '3117', '3118', '3119', '3120', '3121', '3122', '3123', '3124', '3125', '3126', '3127', '3128', '3129', '3130', '3131', '3132', '3133', '3134', '3135', '3136', '3137', '3138', '3139', '3140', '3141', '3142', '3143', '3144', '3145', '3146', '3147', '3148', '3149', '3150', '3151', '3152', '3153', '3154', '3155', '3156', '3157', '3158', '3159', '3160', '3161', '3162', '3163', '3164', '3165', '3166', '3167', '3168', '3169', '3170', '3171', '3172', '3173', '3174', '3175', '3176', '3177', '3178', '3179', '3180', '3181', '3182', '3183', '3184', '3185', '3186', '3187', '3188', '3189', '3190', '3191', '3192', '3193', '3194', '3195', '3196', '3197', '3198', '3199', '3200', '3201', '3202', '3203', '3204', '3205', '3206', '3207', '3208', '3209', '3210', '3211', '3212', '3213', '3214', '3215', '3216', '3217', '3218', '3219', '3220', '3221', '3222', '3223', '3224', '3225', '3226', '3227', '3228', '3229', '3230', '3231', '3232', '3233', '3234', '3235', '3236', '3237', '3238', '3239', '3240', '3241', '3242', '3243', '3244', '3245', '3246', '3247', '3248', '3249', '3250', '3251', '3252', '3253', '3254', '3255', '3256', '3257', '3258', '3259', '3260', '3261', '3262', '3263', '3264', '3265', '3266', '3267', '3268', '3269', '3270', '3271', '3272', '3273', '3274', '3275', '3276', '3277', '3278', '3279', '3280', '3281', '3282', '3283', '3284', '3285', '3286', '3287', '3288', '3289', '3290', '3291', '3292', '3293', '3294', '3295', '3296', '3297', '3298', '3299', '3351', '3352', '3353', '3354', '3355', '3356', '3357', '3358', '3359', '3360', '3361', '3362', '3363', '3364', '3365', '3366', '3367', '3368', '3369', '3370', '3371', '3372', '3373', '3374', '3375', '3376', '3377', '3378', '3379', '3380', '3381', '3382', '3383', '3384', '3385', '3386', '3387', '3388', '3389', '3390', '3391', '3392', '3393', '3394', '3395', '3396', '3397', '3398', '3399', '3400', '3401', '3402', '3403', '3404', '3405', '3406', '3407', '3408', '3409', '3410', '3411', '3412', '3413', '3414', '3415', '3416', '3417', '3418', '3419', '3420', '3421', '3422', '3423', '3424', '3425', '3426', '3427', '3428', '3429', '3430', '3431', '3432', '3433', '3434', '3435', '3436', '3437', '3438', '3439', '3440', '3441', '3501', '3502', '3503', '3504', '3505', '3506', '3507', '3508', '3509', '3510', '3511', '3512', '3513', '3514', '3515', '3516', '3517', '3518', '3519', '3520', '3521', '3522', '3523', '3524', '3525', '3526', '3527', '3528', '3529', '3530', '3531', '3532', '3533', '3534', '3535', '3536', '3537', '3538', '3539', '3540', '3541', '3542', '3543', '3544', '3545', '3546', '3547', '3548', '3549', '3550', '3551', '3552', '3553', '3554', '3555', '3556', '3557', '3558', '3559', '3560', '3561', '3562', '3563', '3564', '3565', '3566', '3567', '3568', '3569', '3570', '3571', '3572', '3573', '3574', '3575', '3576', '3577', '3578', '3579', '3580', '3581', '3582', '3583', '3584', '3585', '3586', '3587', '3588', '3589', '3590', '3591', '3592', '3593', '3594', '3595', '3596', '3597', '3598', '3599', '3600', '3601', '3602', '3603', '3604', '3605', '3606', '3607', '3608', '3609', '3610', '3611', '3612', '3613', '3614', '3615', '3616', '3617', '3618', '3619', '3620', '3621', '3622', '3623', '3624', '3625', '3626', '3627', '3628', '3629', '3630', '3631', '3632', '3633', '3634', '3635', '3636', '3637', '3638', '3639', '3640', '3641', '3642', '3643', '3644', '3645', '3646', '3647', '3648', '3649', '3650', '3651', '3652', '3653', '3654', '3655', '3656', '3657', '3658', '3659', '3660', '3661', '3662', '3663', '3664', '3665', '3666', '3667', '3668', '3669', '3670', '3671', '3672', '3673', '3674', '3675', '3676', '3677', '3678', '3679', '3680', '3681', '3682', '3683', '3684', '3685', '3686', '3687', '3688', '3689', '3690', '3691', '3692', '3693', '3694', '3695', '3696', '3697', '3698', '3699', '3700', '3701', '3702', '3703', '3704', '3705', '3706', '3707', '3708', '3709', '3710', '3711', '3712', '3713', '3714', '3715', '3716', '3717', '3718', '3719', '3720', '3721', '3722', '3723', '3724', '3725', '3726', '3727', '3728', '3729', '3730', '3731', '3732', '3733', '3734', '3735', '3736', '3737', '3738', '3739', '3740', '3741', '3742', '3743', '3744', '3745', '3746', '3747', '3748', '3749', '3750', '3751', '3752', '3753', '3754', '3755', '3756', '3757', '3758', '3759', '3760', '3761', '3762', '3763', '3764', '3765', '3766', '3767', '3768', '3769', '3770', '3771', '3772', '3773', '3774', '3775', '3776', '3777', '3778', '3779', '3780', '3781', '3782', '3783', '3784', '3785', '3786', '3787', '3788', '3789', '3790', '4011', '4111', '4112', '4119', '4121', '4131', '4214', '4225', '4411', '4457', '4468', '4511', '4582', '4723', '4784', '4812', '4814', '4816', '4899', '4900', '5013', '5021', '5039', '5044', '5045', '5046', '5047', '5051', '5065', '5072', '5074', '5085', '5111', '5137', '5139', '5169', '5172', '5192', '5193', '5198', '5199', '5200', '5211', '5231', '5251', '5261', '5271', '5300', '5309', '5310', '5311', '5331', '5399', '5411', '5422', '5441', '5451', '5462', '5499', '5511', '5521', '5531', '5532', '5533', '5551', '5561', '5571', '5592', '5598', '5599', '5611', '5621', '5631', '5641', '5651', '5655', '5661', '5681', '5691', '5697', '5698', '5699', '5712', '5713', '5714', '5718', '5719', '5722', '5732', '5733', '5734', '5735', '5811', '5812', '5813', '5814', '5912', '5931', '5935', '5937', '5940', '5941', '5942', '5943', '5945', '5946', '5947', '5948', '5949', '5950', '5960', '5962', '5963', '5964', '5965', '5966', '5967', '5968', '5969', '5970', '5971', '5972', '5973', '5975', '5976', '5977', '5978', '5983', '5992', '5993', '5994', '5995', '5996', '5997', '5998', '5999', '6300', '6399', '6513', '7011', '7012', '7032', '7033', '7211', '7217', '7221', '7230', '7251', '7261', '7273', '7276', '7277', '7278', '7296', '7297', '7298', '7299', '7311', '7321', '7333', '7338', '7339', '7342', '7349', '7361', '7372', '7375', '7379', '7392', '7393', '7394', '7395', '7399', '7511', '7512', '7513', '7519', '7523', '7534', '7549', '7622', '7623', '7629', '7641', '7692', '7829', '7832', '7841', '7911', '7922', '7929', '7932', '7933', '7941', '7991', '7992', '7993', '7996', '7997', '7998', '7999', '8011', '8021', '8031', '8041', '8042', '8043', '8049', '8050', '8062', '8071', '8099', '8111', '8211', '8220', '8241', '8244', '8249', '8299', '8351', '8641', '8651', '8675', '8699', '8734', '8911', '8931', '8999', '9211', '9222', '9223', '9311', '9399', '9402', '9405']
Transaction_Type_Green = ['ACH', 'ACH', 'ACH', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Cash Advance', 'Cash Payment', 'Cash Advance', 'Cash Payment', 'Cash Advance', 'Cash Payment', 'Cash Advance', 'Cash Payment', 'Cash Advance', 'Cash Payment', 'Wire Transfer', 'Void', 'Refund', 'Wire Transfer', 'Void', 'Refund', 'Wire Transfer', 'Void', 'Refund', 'Payment Reversal']
Country_Green = ['AG', 'AM', 'AU', 'AT', 'BT', 'BQ', 'CA', 'CV', 'CL', 'CX', 'CC', 'DK', 'DJ', 'EE', 'FO', 'FJ', 'DE', 'GL', 'VA', 'HK', 'IS', 'IT', 'LV', 'MU', 'NL', 'NF', 'OM', 'PR', 'AX', 'AS', 'BE', 'FK', 'FI', 'FR', 'GF', 'PF', 'GP', 'GU', 'HU', 'IE', 'LT', 'MQ', 'YT', 'NC', 'MP', 'NO', 'PN', 'PT', 'RE', 'BL', 'SH', 'MF', 'PM', 'SM', 'SI', 'SJ', 'SE', 'CH', 'TV', 'GB', 'US', 'VI', 'WF']

Country_Red = ['AF', 'AO', 'AZ', 'BD', 'BY', 'BZ', 'BO', 'MM', 'KH', 'KM', 'CD', 'CI', 'CU', 'GN', 'GW', 'GY', 'HT', 'ID', 'IR', 'IQ', 'KZ', 'KE', 'KP', 'LA', 'LB', 'LR', 'LY', 'NG', 'PK', 'PG', 'PY', 'SL', 'SX', 'SO', 'SD', 'SY', 'TH', 'TR', 'VE', 'VN', 'YE', 'ZW', 'AL', 'DZ', 'AD', 'AI', 'AR', 'AW', 'BS', 'BJ', 'BM', 'BA', 'BR', 'VG', 'BN', 'BF', 'BI', 'KY', 'CF', 'TD', 'CN', 'CO', 'CK', 'CR', 'CY', 'DM', 'DO', 'EC', 'EG', 'GQ', 'ER', 'GA', 'GM', 'GH', 'GI', 'GR', 'GD', 'GT', 'GG', 'HN', 'IM', 'JP', 'JE', 'JO', 'KR', 'KW', 'KG', 'LI', 'LU', 'MO', 'MG', 'MW', 'MY', 'MV', 'ML', 'MH', 'MR', 'MX', 'MD', 'MC', 'MN', 'MS', 'MA', 'MZ', 'NP', 'NI', 'NE', 'PW', 'PA', 'PE', 'PH', 'RO', 'RU', 'KN', 'LC', 'VC', 'WS', 'ST', 'SA', 'SN', 'SC', 'SB', 'SS', 'LK', 'SR', 'SZ', 'TJ', 'TZ', 'TG', 'TO', 'TT', 'TN', 'TM', 'UG', 'UA', 'UY', 'UZ', 'VU', 'EH', 'ZM']
Merchant_Category_Red = ['4789', '4821', '4829', '5094', '5933', '5944', '6010', '7699', '7994', '7995', '9950']
Transaction_Type_Red = ['Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance',\
'Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance',\
'Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance','Cash Advance',\
'Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment',\
'Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment','Cash Payment',\
'Cash Payment','Cash Payment','Cash Payment','Cash Payment',\
 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', \
'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', 'Purchase', \
 'Payment', 'Payment', 'Payment', 'Payment', 'Payment', 'Wire Transfer', 'Wire Transfer','Wire Transfer','Wire Transfer',\
 'Wire Transfer','Wire Transfer','Wire Transfer','Wire Transfer','Wire Transfer','Wire Transfer','Refund','Refund','Refund',\
 'Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','Refund','ACH','ACH','ACH',\
 'ACH','ACH','ACH','ACH','ACH','ACH','ACH']

All_Merchant_Cat = {'742':'Veterinary Services',
'763':'Agricultural Cooperative',
'780':'Landscaping Services',
'1520':'General Contractors',
'1711':'Heating, Plumbing, A/C',
'1731':'Electrical Contractors',
'1740':'Masonry, Stonework, and Plaster',
'1750':'Carpentry Contractors',
'1761':'Roofing/Siding, Sheet Metal',
'1771':'Concrete Work Contractors',
'1799':'Special Trade Contractors',
'2741':'Miscellaneous Publishing and Printing',
'2791':'Typesetting, Plate Making, and Related Services',
'2842':'Specialty Cleaning',
'3000':'Airlines',
'3001':'Airlines',
'3002':'Airlines',
'3003':'Airlines',
'3004':'Airlines',
'3005':'Airlines',
'3006':'Airlines',
'3007':'Airlines',
'3008':'Airlines',
'3009':'Airlines',
'3010':'Airlines',
'3011':'Airlines',
'3012':'Airlines',
'3013':'Airlines',
'3014':'Airlines',
'3015':'Airlines',
'3016':'Airlines',
'3017':'Airlines',
'3018':'Airlines',
'3019':'Airlines',
'3020':'Airlines',
'3021':'Airlines',
'3022':'Airlines',
'3023':'Airlines',
'3024':'Airlines',
'3025':'Airlines',
'3026':'Airlines',
'3027':'Airlines',
'3028':'Airlines',
'3029':'Airlines',
'3030':'Airlines',
'3031':'Airlines',
'3032':'Airlines',
'3033':'Airlines',
'3034':'Airlines',
'3035':'Airlines',
'3036':'Airlines',
'3037':'Airlines',
'3038':'Airlines',
'3039':'Airlines',
'3040':'Airlines',
'3041':'Airlines',
'3042':'Airlines',
'3043':'Airlines',
'3044':'Airlines',
'3045':'Airlines',
'3046':'Airlines',
'3047':'Airlines',
'3048':'Airlines',
'3049':'Airlines',
'3050':'Airlines',
'3051':'Airlines',
'3052':'Airlines',
'3053':'Airlines',
'3054':'Airlines',
'3055':'Airlines',
'3056':'Airlines',
'3057':'Airlines',
'3058':'Airlines',
'3059':'Airlines',
'3060':'Airlines',
'3061':'Airlines',
'3062':'Airlines',
'3063':'Airlines',
'3064':'Airlines',
'3065':'Airlines',
'3066':'Airlines',
'3067':'Airlines',
'3068':'Airlines',
'3069':'Airlines',
'3070':'Airlines',
'3071':'Airlines',
'3072':'Airlines',
'3073':'Airlines',
'3074':'Airlines',
'3075':'Airlines',
'3076':'Airlines',
'3077':'Airlines',
'3078':'Airlines',
'3079':'Airlines',
'3080':'Airlines',
'3081':'Airlines',
'3082':'Airlines',
'3083':'Airlines',
'3084':'Airlines',
'3085':'Airlines',
'3086':'Airlines',
'3087':'Airlines',
'3088':'Airlines',
'3089':'Airlines',
'3090':'Airlines',
'3091':'Airlines',
'3092':'Airlines',
'3093':'Airlines',
'3094':'Airlines',
'3095':'Airlines',
'3096':'Airlines',
'3097':'Airlines',
'3098':'Airlines',
'3099':'Airlines',
'3100':'Airlines',
'3101':'Airlines',
'3102':'Airlines',
'3103':'Airlines',
'3104':'Airlines',
'3105':'Airlines',
'3106':'Airlines',
'3107':'Airlines',
'3108':'Airlines',
'3109':'Airlines',
'3110':'Airlines',
'3111':'Airlines',
'3112':'Airlines',
'3113':'Airlines',
'3114':'Airlines',
'3115':'Airlines',
'3116':'Airlines',
'3117':'Airlines',
'3118':'Airlines',
'3119':'Airlines',
'3120':'Airlines',
'3121':'Airlines',
'3122':'Airlines',
'3123':'Airlines',
'3124':'Airlines',
'3125':'Airlines',
'3126':'Airlines',
'3127':'Airlines',
'3128':'Airlines',
'3129':'Airlines',
'3130':'Airlines',
'3131':'Airlines',
'3132':'Airlines',
'3133':'Airlines',
'3134':'Airlines',
'3135':'Airlines',
'3136':'Airlines',
'3137':'Airlines',
'3138':'Airlines',
'3139':'Airlines',
'3140':'Airlines',
'3141':'Airlines',
'3142':'Airlines',
'3143':'Airlines',
'3144':'Airlines',
'3145':'Airlines',
'3146':'Airlines',
'3147':'Airlines',
'3148':'Airlines',
'3149':'Airlines',
'3150':'Airlines',
'3151':'Airlines',
'3152':'Airlines',
'3153':'Airlines',
'3154':'Airlines',
'3155':'Airlines',
'3156':'Airlines',
'3157':'Airlines',
'3158':'Airlines',
'3159':'Airlines',
'3160':'Airlines',
'3161':'Airlines',
'3162':'Airlines',
'3163':'Airlines',
'3164':'Airlines',
'3165':'Airlines',
'3166':'Airlines',
'3167':'Airlines',
'3168':'Airlines',
'3169':'Airlines',
'3170':'Airlines',
'3171':'Airlines',
'3172':'Airlines',
'3173':'Airlines',
'3174':'Airlines',
'3175':'Airlines',
'3176':'Airlines',
'3177':'Airlines',
'3178':'Airlines',
'3179':'Airlines',
'3180':'Airlines',
'3181':'Airlines',
'3182':'Airlines',
'3183':'Airlines',
'3184':'Airlines',
'3185':'Airlines',
'3186':'Airlines',
'3187':'Airlines',
'3188':'Airlines',
'3189':'Airlines',
'3190':'Airlines',
'3191':'Airlines',
'3192':'Airlines',
'3193':'Airlines',
'3194':'Airlines',
'3195':'Airlines',
'3196':'Airlines',
'3197':'Airlines',
'3198':'Airlines',
'3199':'Airlines',
'3200':'Airlines',
'3201':'Airlines',
'3202':'Airlines',
'3203':'Airlines',
'3204':'Airlines',
'3205':'Airlines',
'3206':'Airlines',
'3207':'Airlines',
'3208':'Airlines',
'3209':'Airlines',
'3210':'Airlines',
'3211':'Airlines',
'3212':'Airlines',
'3213':'Airlines',
'3214':'Airlines',
'3215':'Airlines',
'3216':'Airlines',
'3217':'Airlines',
'3218':'Airlines',
'3219':'Airlines',
'3220':'Airlines',
'3221':'Airlines',
'3222':'Airlines',
'3223':'Airlines',
'3224':'Airlines',
'3225':'Airlines',
'3226':'Airlines',
'3227':'Airlines',
'3228':'Airlines',
'3229':'Airlines',
'3230':'Airlines',
'3231':'Airlines',
'3232':'Airlines',
'3233':'Airlines',
'3234':'Airlines',
'3235':'Airlines',
'3236':'Airlines',
'3237':'Airlines',
'3238':'Airlines',
'3239':'Airlines',
'3240':'Airlines',
'3241':'Airlines',
'3242':'Airlines',
'3243':'Airlines',
'3244':'Airlines',
'3245':'Airlines',
'3246':'Airlines',
'3247':'Airlines',
'3248':'Airlines',
'3249':'Airlines',
'3250':'Airlines',
'3251':'Airlines',
'3252':'Airlines',
'3253':'Airlines',
'3254':'Airlines',
'3255':'Airlines',
'3256':'Airlines',
'3257':'Airlines',
'3258':'Airlines',
'3259':'Airlines',
'3260':'Airlines',
'3261':'Airlines',
'3262':'Airlines',
'3263':'Airlines',
'3264':'Airlines',
'3265':'Airlines',
'3266':'Airlines',
'3267':'Airlines',
'3268':'Airlines',
'3269':'Airlines',
'3270':'Airlines',
'3271':'Airlines',
'3272':'Airlines',
'3273':'Airlines',
'3274':'Airlines',
'3275':'Airlines',
'3276':'Airlines',
'3277':'Airlines',
'3278':'Airlines',
'3279':'Airlines',
'3280':'Airlines',
'3281':'Airlines',
'3282':'Airlines',
'3283':'Airlines',
'3284':'Airlines',
'3285':'Airlines',
'3286':'Airlines',
'3287':'Airlines',
'3288':'Airlines',
'3289':'Airlines',
'3290':'Airlines',
'3291':'Airlines',
'3292':'Airlines',
'3293':'Airlines',
'3294':'Airlines',
'3295':'Airlines',
'3296':'Airlines',
'3297':'Airlines',
'3298':'Airlines',
'3299':'Airlines',
'3351':'Car Rental',
'3352':'Car Rental',
'3353':'Car Rental',
'3354':'Car Rental',
'3355':'Car Rental',
'3356':'Car Rental',
'3357':'Car Rental',
'3358':'Car Rental',
'3359':'Car Rental',
'3360':'Car Rental',
'3361':'Car Rental',
'3362':'Car Rental',
'3363':'Car Rental',
'3364':'Car Rental',
'3365':'Car Rental',
'3366':'Car Rental',
'3367':'Car Rental',
'3368':'Car Rental',
'3369':'Car Rental',
'3370':'Car Rental',
'3371':'Car Rental',
'3372':'Car Rental',
'3373':'Car Rental',
'3374':'Car Rental',
'3375':'Car Rental',
'3376':'Car Rental',
'3377':'Car Rental',
'3378':'Car Rental',
'3379':'Car Rental',
'3380':'Car Rental',
'3381':'Car Rental',
'3382':'Car Rental',
'3383':'Car Rental',
'3384':'Car Rental',
'3385':'Car Rental',
'3386':'Car Rental',
'3387':'Car Rental',
'3388':'Car Rental',
'3389':'Car Rental',
'3390':'Car Rental',
'3391':'Car Rental',
'3392':'Car Rental',
'3393':'Car Rental',
'3394':'Car Rental',
'3395':'Car Rental',
'3396':'Car Rental',
'3397':'Car Rental',
'3398':'Car Rental',
'3399':'Car Rental',
'3400':'Car Rental',
'3401':'Car Rental',
'3402':'Car Rental',
'3403':'Car Rental',
'3404':'Car Rental',
'3405':'Car Rental',
'3406':'Car Rental',
'3407':'Car Rental',
'3408':'Car Rental',
'3409':'Car Rental',
'3410':'Car Rental',
'3411':'Car Rental',
'3412':'Car Rental',
'3413':'Car Rental',
'3414':'Car Rental',
'3415':'Car Rental',
'3416':'Car Rental',
'3417':'Car Rental',
'3418':'Car Rental',
'3419':'Car Rental',
'3420':'Car Rental',
'3421':'Car Rental',
'3422':'Car Rental',
'3423':'Car Rental',
'3424':'Car Rental',
'3425':'Car Rental',
'3426':'Car Rental',
'3427':'Car Rental',
'3428':'Car Rental',
'3429':'Car Rental',
'3430':'Car Rental',
'3431':'Car Rental',
'3432':'Car Rental',
'3433':'Car Rental',
'3434':'Car Rental',
'3435':'Car Rental',
'3436':'Car Rental',
'3437':'Car Rental',
'3438':'Car Rental',
'3439':'Car Rental',
'3440':'Car Rental',
'3441':'Car Rental',
'3501':'Hotels/Motels/Inns/Resorts',
'3502':'Hotels/Motels/Inns/Resorts',
'3503':'Hotels/Motels/Inns/Resorts',
'3504':'Hotels/Motels/Inns/Resorts',
'3505':'Hotels/Motels/Inns/Resorts',
'3506':'Hotels/Motels/Inns/Resorts',
'3507':'Hotels/Motels/Inns/Resorts',
'3508':'Hotels/Motels/Inns/Resorts',
'3509':'Hotels/Motels/Inns/Resorts',
'3510':'Hotels/Motels/Inns/Resorts',
'3511':'Hotels/Motels/Inns/Resorts',
'3512':'Hotels/Motels/Inns/Resorts',
'3513':'Hotels/Motels/Inns/Resorts',
'3514':'Hotels/Motels/Inns/Resorts',
'3515':'Hotels/Motels/Inns/Resorts',
'3516':'Hotels/Motels/Inns/Resorts',
'3517':'Hotels/Motels/Inns/Resorts',
'3518':'Hotels/Motels/Inns/Resorts',
'3519':'Hotels/Motels/Inns/Resorts',
'3520':'Hotels/Motels/Inns/Resorts',
'3521':'Hotels/Motels/Inns/Resorts',
'3522':'Hotels/Motels/Inns/Resorts',
'3523':'Hotels/Motels/Inns/Resorts',
'3524':'Hotels/Motels/Inns/Resorts',
'3525':'Hotels/Motels/Inns/Resorts',
'3526':'Hotels/Motels/Inns/Resorts',
'3527':'Hotels/Motels/Inns/Resorts',
'3528':'Hotels/Motels/Inns/Resorts',
'3529':'Hotels/Motels/Inns/Resorts',
'3530':'Hotels/Motels/Inns/Resorts',
'3531':'Hotels/Motels/Inns/Resorts',
'3532':'Hotels/Motels/Inns/Resorts',
'3533':'Hotels/Motels/Inns/Resorts',
'3534':'Hotels/Motels/Inns/Resorts',
'3535':'Hotels/Motels/Inns/Resorts',
'3536':'Hotels/Motels/Inns/Resorts',
'3537':'Hotels/Motels/Inns/Resorts',
'3538':'Hotels/Motels/Inns/Resorts',
'3539':'Hotels/Motels/Inns/Resorts',
'3540':'Hotels/Motels/Inns/Resorts',
'3541':'Hotels/Motels/Inns/Resorts',
'3542':'Hotels/Motels/Inns/Resorts',
'3543':'Hotels/Motels/Inns/Resorts',
'3544':'Hotels/Motels/Inns/Resorts',
'3545':'Hotels/Motels/Inns/Resorts',
'3546':'Hotels/Motels/Inns/Resorts',
'3547':'Hotels/Motels/Inns/Resorts',
'3548':'Hotels/Motels/Inns/Resorts',
'3549':'Hotels/Motels/Inns/Resorts',
'3550':'Hotels/Motels/Inns/Resorts',
'3551':'Hotels/Motels/Inns/Resorts',
'3552':'Hotels/Motels/Inns/Resorts',
'3553':'Hotels/Motels/Inns/Resorts',
'3554':'Hotels/Motels/Inns/Resorts',
'3555':'Hotels/Motels/Inns/Resorts',
'3556':'Hotels/Motels/Inns/Resorts',
'3557':'Hotels/Motels/Inns/Resorts',
'3558':'Hotels/Motels/Inns/Resorts',
'3559':'Hotels/Motels/Inns/Resorts',
'3560':'Hotels/Motels/Inns/Resorts',
'3561':'Hotels/Motels/Inns/Resorts',
'3562':'Hotels/Motels/Inns/Resorts',
'3563':'Hotels/Motels/Inns/Resorts',
'3564':'Hotels/Motels/Inns/Resorts',
'3565':'Hotels/Motels/Inns/Resorts',
'3566':'Hotels/Motels/Inns/Resorts',
'3567':'Hotels/Motels/Inns/Resorts',
'3568':'Hotels/Motels/Inns/Resorts',
'3569':'Hotels/Motels/Inns/Resorts',
'3570':'Hotels/Motels/Inns/Resorts',
'3571':'Hotels/Motels/Inns/Resorts',
'3572':'Hotels/Motels/Inns/Resorts',
'3573':'Hotels/Motels/Inns/Resorts',
'3574':'Hotels/Motels/Inns/Resorts',
'3575':'Hotels/Motels/Inns/Resorts',
'3576':'Hotels/Motels/Inns/Resorts',
'3577':'Hotels/Motels/Inns/Resorts',
'3578':'Hotels/Motels/Inns/Resorts',
'3579':'Hotels/Motels/Inns/Resorts',
'3580':'Hotels/Motels/Inns/Resorts',
'3581':'Hotels/Motels/Inns/Resorts',
'3582':'Hotels/Motels/Inns/Resorts',
'3583':'Hotels/Motels/Inns/Resorts',
'3584':'Hotels/Motels/Inns/Resorts',
'3585':'Hotels/Motels/Inns/Resorts',
'3586':'Hotels/Motels/Inns/Resorts',
'3587':'Hotels/Motels/Inns/Resorts',
'3588':'Hotels/Motels/Inns/Resorts',
'3589':'Hotels/Motels/Inns/Resorts',
'3590':'Hotels/Motels/Inns/Resorts',
'3591':'Hotels/Motels/Inns/Resorts',
'3592':'Hotels/Motels/Inns/Resorts',
'3593':'Hotels/Motels/Inns/Resorts',
'3594':'Hotels/Motels/Inns/Resorts',
'3595':'Hotels/Motels/Inns/Resorts',
'3596':'Hotels/Motels/Inns/Resorts',
'3597':'Hotels/Motels/Inns/Resorts',
'3598':'Hotels/Motels/Inns/Resorts',
'3599':'Hotels/Motels/Inns/Resorts',
'3600':'Hotels/Motels/Inns/Resorts',
'3601':'Hotels/Motels/Inns/Resorts',
'3602':'Hotels/Motels/Inns/Resorts',
'3603':'Hotels/Motels/Inns/Resorts',
'3604':'Hotels/Motels/Inns/Resorts',
'3605':'Hotels/Motels/Inns/Resorts',
'3606':'Hotels/Motels/Inns/Resorts',
'3607':'Hotels/Motels/Inns/Resorts',
'3608':'Hotels/Motels/Inns/Resorts',
'3609':'Hotels/Motels/Inns/Resorts',
'3610':'Hotels/Motels/Inns/Resorts',
'3611':'Hotels/Motels/Inns/Resorts',
'3612':'Hotels/Motels/Inns/Resorts',
'3613':'Hotels/Motels/Inns/Resorts',
'3614':'Hotels/Motels/Inns/Resorts',
'3615':'Hotels/Motels/Inns/Resorts',
'3616':'Hotels/Motels/Inns/Resorts',
'3617':'Hotels/Motels/Inns/Resorts',
'3618':'Hotels/Motels/Inns/Resorts',
'3619':'Hotels/Motels/Inns/Resorts',
'3620':'Hotels/Motels/Inns/Resorts',
'3621':'Hotels/Motels/Inns/Resorts',
'3622':'Hotels/Motels/Inns/Resorts',
'3623':'Hotels/Motels/Inns/Resorts',
'3624':'Hotels/Motels/Inns/Resorts',
'3625':'Hotels/Motels/Inns/Resorts',
'3626':'Hotels/Motels/Inns/Resorts',
'3627':'Hotels/Motels/Inns/Resorts',
'3628':'Hotels/Motels/Inns/Resorts',
'3629':'Hotels/Motels/Inns/Resorts',
'3630':'Hotels/Motels/Inns/Resorts',
'3631':'Hotels/Motels/Inns/Resorts',
'3632':'Hotels/Motels/Inns/Resorts',
'3633':'Hotels/Motels/Inns/Resorts',
'3634':'Hotels/Motels/Inns/Resorts',
'3635':'Hotels/Motels/Inns/Resorts',
'3636':'Hotels/Motels/Inns/Resorts',
'3637':'Hotels/Motels/Inns/Resorts',
'3638':'Hotels/Motels/Inns/Resorts',
'3639':'Hotels/Motels/Inns/Resorts',
'3640':'Hotels/Motels/Inns/Resorts',
'3641':'Hotels/Motels/Inns/Resorts',
'3642':'Hotels/Motels/Inns/Resorts',
'3643':'Hotels/Motels/Inns/Resorts',
'3644':'Hotels/Motels/Inns/Resorts',
'3645':'Hotels/Motels/Inns/Resorts',
'3646':'Hotels/Motels/Inns/Resorts',
'3647':'Hotels/Motels/Inns/Resorts',
'3648':'Hotels/Motels/Inns/Resorts',
'3649':'Hotels/Motels/Inns/Resorts',
'3650':'Hotels/Motels/Inns/Resorts',
'3651':'Hotels/Motels/Inns/Resorts',
'3652':'Hotels/Motels/Inns/Resorts',
'3653':'Hotels/Motels/Inns/Resorts',
'3654':'Hotels/Motels/Inns/Resorts',
'3655':'Hotels/Motels/Inns/Resorts',
'3656':'Hotels/Motels/Inns/Resorts',
'3657':'Hotels/Motels/Inns/Resorts',
'3658':'Hotels/Motels/Inns/Resorts',
'3659':'Hotels/Motels/Inns/Resorts',
'3660':'Hotels/Motels/Inns/Resorts',
'3661':'Hotels/Motels/Inns/Resorts',
'3662':'Hotels/Motels/Inns/Resorts',
'3663':'Hotels/Motels/Inns/Resorts',
'3664':'Hotels/Motels/Inns/Resorts',
'3665':'Hotels/Motels/Inns/Resorts',
'3666':'Hotels/Motels/Inns/Resorts',
'3667':'Hotels/Motels/Inns/Resorts',
'3668':'Hotels/Motels/Inns/Resorts',
'3669':'Hotels/Motels/Inns/Resorts',
'3670':'Hotels/Motels/Inns/Resorts',
'3671':'Hotels/Motels/Inns/Resorts',
'3672':'Hotels/Motels/Inns/Resorts',
'3673':'Hotels/Motels/Inns/Resorts',
'3674':'Hotels/Motels/Inns/Resorts',
'3675':'Hotels/Motels/Inns/Resorts',
'3676':'Hotels/Motels/Inns/Resorts',
'3677':'Hotels/Motels/Inns/Resorts',
'3678':'Hotels/Motels/Inns/Resorts',
'3679':'Hotels/Motels/Inns/Resorts',
'3680':'Hotels/Motels/Inns/Resorts',
'3681':'Hotels/Motels/Inns/Resorts',
'3682':'Hotels/Motels/Inns/Resorts',
'3683':'Hotels/Motels/Inns/Resorts',
'3684':'Hotels/Motels/Inns/Resorts',
'3685':'Hotels/Motels/Inns/Resorts',
'3686':'Hotels/Motels/Inns/Resorts',
'3687':'Hotels/Motels/Inns/Resorts',
'3688':'Hotels/Motels/Inns/Resorts',
'3689':'Hotels/Motels/Inns/Resorts',
'3690':'Hotels/Motels/Inns/Resorts',
'3691':'Hotels/Motels/Inns/Resorts',
'3692':'Hotels/Motels/Inns/Resorts',
'3693':'Hotels/Motels/Inns/Resorts',
'3694':'Hotels/Motels/Inns/Resorts',
'3695':'Hotels/Motels/Inns/Resorts',
'3696':'Hotels/Motels/Inns/Resorts',
'3697':'Hotels/Motels/Inns/Resorts',
'3698':'Hotels/Motels/Inns/Resorts',
'3699':'Hotels/Motels/Inns/Resorts',
'3700':'Hotels/Motels/Inns/Resorts',
'3701':'Hotels/Motels/Inns/Resorts',
'3702':'Hotels/Motels/Inns/Resorts',
'3703':'Hotels/Motels/Inns/Resorts',
'3704':'Hotels/Motels/Inns/Resorts',
'3705':'Hotels/Motels/Inns/Resorts',
'3706':'Hotels/Motels/Inns/Resorts',
'3707':'Hotels/Motels/Inns/Resorts',
'3708':'Hotels/Motels/Inns/Resorts',
'3709':'Hotels/Motels/Inns/Resorts',
'3710':'Hotels/Motels/Inns/Resorts',
'3711':'Hotels/Motels/Inns/Resorts',
'3712':'Hotels/Motels/Inns/Resorts',
'3713':'Hotels/Motels/Inns/Resorts',
'3714':'Hotels/Motels/Inns/Resorts',
'3715':'Hotels/Motels/Inns/Resorts',
'3716':'Hotels/Motels/Inns/Resorts',
'3717':'Hotels/Motels/Inns/Resorts',
'3718':'Hotels/Motels/Inns/Resorts',
'3719':'Hotels/Motels/Inns/Resorts',
'3720':'Hotels/Motels/Inns/Resorts',
'3721':'Hotels/Motels/Inns/Resorts',
'3722':'Hotels/Motels/Inns/Resorts',
'3723':'Hotels/Motels/Inns/Resorts',
'3724':'Hotels/Motels/Inns/Resorts',
'3725':'Hotels/Motels/Inns/Resorts',
'3726':'Hotels/Motels/Inns/Resorts',
'3727':'Hotels/Motels/Inns/Resorts',
'3728':'Hotels/Motels/Inns/Resorts',
'3729':'Hotels/Motels/Inns/Resorts',
'3730':'Hotels/Motels/Inns/Resorts',
'3731':'Hotels/Motels/Inns/Resorts',
'3732':'Hotels/Motels/Inns/Resorts',
'3733':'Hotels/Motels/Inns/Resorts',
'3734':'Hotels/Motels/Inns/Resorts',
'3735':'Hotels/Motels/Inns/Resorts',
'3736':'Hotels/Motels/Inns/Resorts',
'3737':'Hotels/Motels/Inns/Resorts',
'3738':'Hotels/Motels/Inns/Resorts',
'3739':'Hotels/Motels/Inns/Resorts',
'3740':'Hotels/Motels/Inns/Resorts',
'3741':'Hotels/Motels/Inns/Resorts',
'3742':'Hotels/Motels/Inns/Resorts',
'3743':'Hotels/Motels/Inns/Resorts',
'3744':'Hotels/Motels/Inns/Resorts',
'3745':'Hotels/Motels/Inns/Resorts',
'3746':'Hotels/Motels/Inns/Resorts',
'3747':'Hotels/Motels/Inns/Resorts',
'3748':'Hotels/Motels/Inns/Resorts',
'3749':'Hotels/Motels/Inns/Resorts',
'3750':'Hotels/Motels/Inns/Resorts',
'3751':'Hotels/Motels/Inns/Resorts',
'3752':'Hotels/Motels/Inns/Resorts',
'3753':'Hotels/Motels/Inns/Resorts',
'3754':'Hotels/Motels/Inns/Resorts',
'3755':'Hotels/Motels/Inns/Resorts',
'3756':'Hotels/Motels/Inns/Resorts',
'3757':'Hotels/Motels/Inns/Resorts',
'3758':'Hotels/Motels/Inns/Resorts',
'3759':'Hotels/Motels/Inns/Resorts',
'3760':'Hotels/Motels/Inns/Resorts',
'3761':'Hotels/Motels/Inns/Resorts',
'3762':'Hotels/Motels/Inns/Resorts',
'3763':'Hotels/Motels/Inns/Resorts',
'3764':'Hotels/Motels/Inns/Resorts',
'3765':'Hotels/Motels/Inns/Resorts',
'3766':'Hotels/Motels/Inns/Resorts',
'3767':'Hotels/Motels/Inns/Resorts',
'3768':'Hotels/Motels/Inns/Resorts',
'3769':'Hotels/Motels/Inns/Resorts',
'3770':'Hotels/Motels/Inns/Resorts',
'3771':'Hotels/Motels/Inns/Resorts',
'3772':'Hotels/Motels/Inns/Resorts',
'3773':'Hotels/Motels/Inns/Resorts',
'3774':'Hotels/Motels/Inns/Resorts',
'3775':'Hotels/Motels/Inns/Resorts',
'3776':'Hotels/Motels/Inns/Resorts',
'3777':'Hotels/Motels/Inns/Resorts',
'3778':'Hotels/Motels/Inns/Resorts',
'3779':'Hotels/Motels/Inns/Resorts',
'3780':'Hotels/Motels/Inns/Resorts',
'3781':'Hotels/Motels/Inns/Resorts',
'3782':'Hotels/Motels/Inns/Resorts',
'3783':'Hotels/Motels/Inns/Resorts',
'3784':'Hotels/Motels/Inns/Resorts',
'3785':'Hotels/Motels/Inns/Resorts',
'3786':'Hotels/Motels/Inns/Resorts',
'3787':'Hotels/Motels/Inns/Resorts',
'3788':'Hotels/Motels/Inns/Resorts',
'3789':'Hotels/Motels/Inns/Resorts',
'3790':'Hotels/Motels/Inns/Resorts',
'4011':'Railroads',
'4111':'Commuter Transport, Ferries',
'4112':'Passenger Railways',
'4119':'Ambulance Services',
'4121':'Taxicabs/Limousines',
'4131':'Bus Lines',
'4214':'Motor Freight Carriers and Trucking Local and Long Distance Moving and Storage Companies and Local Delivery Services',
'4215':'Courier Services',
'4225':'Public Warehousing and Storage Farm Products Refrigerated Goods Household Goods and Storage',
'4411':'Cruise Lines',
'4457':'Boat Rentals and Leases',
'4468':'Marinas/ Service and Supplies',
'4511':'Airlines/ Air Carriers',
'4582':'Airports/ Flying Fields',
'4722':'Travel Agencies/ Tour Operators',
'4723':'TUI Travel - Germany',
'4784':'Tolls/Bridge Fees',
'4789':'Transportation Services (Not Elsewhere Classified)',
'4812':'Telecommunication Equipment and Telephone Sales',
'4814':'Telecommunication Services',
'4816':'Computer Network Services',
'4821':'Telegraph Services',
'4829':'Wires, Money Orders',
'4899':'Cable/ Satellite, and Other Pay Television and Radio',
'4900':'Utilities',
'5013':'Motor Vehicle Supplies and New Parts',
'5021':'Office and Commercial Furniture',
'5039':'Construction Materials (Not Elsewhere Classified)',
'5044':'Photographic, Photocopy, Microfilm Equipment, and Supplies',
'5045':'Computers, Peripherals, and Software',
'5046':'Commercial Equipment (Not Elsewhere Classified)',
'5047':'Medical, Dental, Ophthalmic, and Hospital Equipment and Supplies',
'5051':'Metal Service Centers',
'5065':'Electrical Parts and Equipment',
'5072':'Hardware, Equipment, and Supplies',
'5074':'Plumbing, Heating Equipment, and Supplies',
'5085':'Industrial Supplies (Not Elsewhere Classified)',
'5094':'Precious Stones and Metals, Watches and Jewelry',
'5099':'Durable Goods (Not Elsewhere Classified)',
'5111':'Stationary, Office Supplies, Printing and Writing Paper',
'5122':'Drugs, Drug Proprietaries, and Druggist Sundries',
'5131':'Piece Goods, Notions, and Other Dry Goods',
'5137':'Uniforms, Commercial Clothing',
'5139':'Commercial Footwear',
'5169':'Chemicals and Allied Products (Not Elsewhere Classified)',
'5172':'Petroleum and Petroleum Products',
'5192':'Books, Periodicals, and Newspapers',
'5193':'Florists Supplies, Nursery Stock, and Flowers',
'5198':'Paints, Varnishes, and Supplies',
'5199':'Nondurable Goods (Not Elsewhere Classified)',
'5200':'Home Supply Warehouse Stores',
'5211':'Lumber, Building Materials Stores',
'5231':'Glass, Paint, and Wallpaper Stores',
'5251':'Hardware Stores',
'5261':'Nurseries, Lawn and Garden Supply Stores',
'5271':'Mobile Home Dealers',
'5300':'Wholesale Clubs',
'5309':'Duty Free Stores',
'5310':'Discount Stores',
'5311':'Department Stores',
'5331':'Variety Stores',
'5399':'Miscellaneous General Merchandise',
'5411':'Grocery Stores, Supermarkets',
'5422':'Freezer and Locker Meat Provisioners',
'5441':'Candy, Nut, and Confectionery Stores',
'5451':'Dairy Products Stores',
'5462':'Bakeries',
'5499':'Miscellaneous Food Stores  Convenience Stores and Specialty Markets',
'5511':'Car & Truck Dealers (New / Used) Sales, Service, Repairs Parts and Leasing',
'5521':'Car & Truck Dealers (Used Only) Sales, Service, Repairs Parts and Leasing',
'5531':'Auto and Home Supply Stores',
'5532':'Automotive Tire Stores',
'5533':'Automotive Parts and Accessories Stores',
'5541':'Service Stations',
'5542':'Automated Fuel Dispensers',
'5551':'Boat Dealers',
'5561':'Camper, Recreational and Utility Trailer Dealers',
'5571':'Motorcycle Shops and Dealers',
'5592':'Motor Homes Dealers',
'5598':'Snowmobile Dealers',
'5599':'Miscellaneous Auto Dealers',
'5611':'Mens and Boys Clothing and Accessories Stores',
'5621':'Womens Ready-To-Wear Stores',
'5631':'Womens Accessory and Specialty Shops',
'5641':'Childrens and Infants Wear Stores',
'5651':'Family Clothing Stores',
'5655':'Sports and Riding Apparel Stores',
'5661':'Shoe Stores',
'5681':'Furriers and Fur Shops',
'5691':'Mens, Womens Clothing Stores',
'5697':'Tailors, Alterations',
'5698':'Wig and Toupee Stores',
'5699':'Miscellaneous Apparel and Accessory Shops',
'5712':'Furniture, Home Furnishings, and Equipment Stores, Except Appliances',
'5713':'Floor Covering Stores',
'5714':'Drapery, Window Covering, and Upholstery Stores',
'5718':'Fireplace, Fireplace Screens, and Accessories Stores',
'5719':'Miscellaneous Home Furnishing Specialty Stores',
'5722':'Household Appliance Stores',
'5732':'Electronics Stores',
'5733':'Music Stores-Musical Instruments, Pianos, and Sheet Music',
'5734':'Computer Software Stores',
'5735':'Record Stores',
'5811':'Caterers',
'5812':'Eating Places, Restaurants',
'5813':'Drinking Places',
'5814':'Fast Food Restaurants',
'5912':'Drug Stores and Pharmacies',
'5921':'Package Stores/Beer, Wine, and Liquor',
'5931':'Used Merchandise and Secondhand Stores',
'5932':'Antique Shops',
'5933':'Pawn Shops',
'5935':'Wrecking and Salvage Yards',
'5937':'Antique Reproductions',
'5940':'Bicycle Shops',
'5941':'Sporting Goods Stores',
'5942':'Book Stores',
'5943':'Stationery Stores, Office, and School Supply Stores',
'5944':'Jewelry Stores, Watches, Clocks, and Silverware Stores',
'5945':'Hobby, Toy, and Game Shops',
'5946':'Camera and Photographic Supply Stores',
'5947':'Gift, Card, Novelty, and Souvenir Shops',
'5948':'Luggage and Leather Goods Stores',
'5949':'Sewing, Needlework, Fabric, and Piece Goods Stores',
'5950':'Glassware, Crystal Stores',
'5960':'Direct Marketing   Insurance Services',
'5962':'Direct Marketing   Travel',
'5963':'Door To Door Sales',
'5964':'Direct Marketing   Catalog Merchant',
'5965':'Direct Marketing   Combination Catalog and Retail Merchant',
'5966':'Direct Marketing   Outbound Tele',
'5967':'Direct Marketing   Inbound Tele',
'5968':'Direct Marketing   Subscription',
'5969':'Direct Marketing   Other',
'5970':'Artists Supply and Craft Shops',
'5971':'Art Dealers and Galleries',
'5972':'Stamp and Coin Stores',
'5973':'Religious Goods Stores',
'5975':'Hearing Aids Sales and Supplies',
'5976':'Orthopedic Goods   Prosthetic Devices',
'5977':'Cosmetic Stores',
'5978':'Typewriter Stores',
'5983':'Fuel Dealers (Non Automotive)',
'5992':'Florists',
'5993':'Cigar Stores and Stands',
'5994':'News Dealers and Newsstands',
'5995':'Pet Shops, Pet Food, and Supplies',
'5996':'Swimming Pools Sales',
'5997':'Electric Razor Stores',
'5998':'Tent and Awning Shops',
'5999':'Miscellaneous Specialty Retail',
'6010':'Manual Cash Disburse',
'6011':'Automated Cash Disburse',
'6012':'Financial Institutions',
'6051':'Non Fl, Money Orders',
'6211':'Security Brokers/Dealers',
'6300':'Insurance Underwriting, Premiums',
'6399':'Insurance   Default',
'6513':'Real Estate Agents and Managers - Rentals',
'7011':'Hotels, Motels, and Resorts',
'7012':'Timeshares',
'7032':'Sporting/Recreation Camps',
'7033':'Trailer Parks, Campgrounds',
'7210':'Laundry, Cleaning Services',
'7211':'Laundries',
'7216':'Dry Cleaners',
'7217':'Carpet/Upholstery Cleaning',
'7221':'Photographic Studios',
'7230':'Barber and Beauty Shops',
'7251':'Shoe Repair/Hat Cleaning',
'7261':'Funeral Services, Crematories',
'7273':'Dating/Escort Services',
'7276':'Tax Preparation Services',
'7277':'Counseling Services',
'7278':'Buying/Shopping Services',
'7296':'Clothing Rental',
'7297':'Massage Parlors',
'7298':'Health and Beauty Spas',
'7299':'Miscellaneous General Services',
'7311':'Advertising Services',
'7321':'Credit Reporting Agencies',
'7333':'Commercial Photography, Art and Graphics',
'7338':'Quick Copy, Repro, and Blueprint',
'7339':'Secretarial Support Services',
'7342':'Exterminating Services',
'7349':'Cleaning and Maintenance',
'7361':'Employment/Temp Agencies',
'7372':'Computer Programming',
'7375':'Information Retrieval Services',
'7379':'Computer Repair',
'7392':'Consulting, Public Relations',
'7393':'Detective Agencies',
'7394':'Equipment Rental',
'7395':'Photo Developing',
'7399':'Miscellaneous Business Services',
'7511':'Truck Stop',
'7512':'Car Rental Agencies',
'7513':'Truck/Utility Trailer Rentals',
'7519':'Recreational Vehicle Rentals',
'7523':'Parking Lots, Garages',
'7531':'Auto Body Repair Shops',
'7534':'Tire Retreading and Repair',
'7535':'Auto Paint Shops',
'7538':'Auto Service Shops',
'7542':'Car Washes',
'7549':'Towing Services',
'7622':'Electronics Repair Shops',
'7623':'A/C, Refrigeration Repair',
'7629':'Small Appliance Repair',
'7631':'Watch/Jewelry Repair',
'7641':'Furniture Repair, Refinishing',
'7692':'Welding Repair',
'7699':'Miscellaneous Repair Shops',
'7829':'Picture/Video Production',
'7832':'Motion Picture Theaters',
'7841':'Video Tape Rental Stores',
'7911':'Dance Hall, Studios, Schools',
'7922':'Theatrical Ticket Agencies',
'7929':'Bands, Orchestras',
'7932':'Billiard/Pool Establishments',
'7933':'Bowling Alleys',
'7941':'Sports Clubs/Fields',
'7991':'Tourist Attractions and Exhibits',
'7992':'Golf Courses   Public',
'7993':'Video Amusement Game Supplies',
'7994':'Video Game Arcades',
'7995':'Betting/Casino Gambling',
'7996':'Amusement Parks/Carnivals',
'7997':'Country_Green Clubs',
'7998':'Aquariums',
'7999':'Miscellaneous Recreation Services',
'8011':'Doctors',
'8021':'Dentists, Orthodontists',
'8031':'Osteopaths',
'8041':'Chiropractors',
'8042':'Optometrists, Ophthalmologists',
'8043':'Opticians, Eyeglasses',
'8049':'Chiropodists, Podiatrists',
'8050':'Nursing/Personal Care',
'8062':'Hospitals',
'8071':'Medical and Dental Labs',
'8099':'Medical Services',
'8111':'Legal Services, Attorneys',
'8211':'Elementary, Secondary Schools',
'8220':'Colleges, Universities',
'8241':'Correspondence Schools',
'8244':'Business/Secretarial Schools',
'8249':'Vocational/Trade Schools',
'8299':'Educational Services',
'8351':'Child Care Services',
'8398':'Charitable and Social Service Organizations   Fundraising',
'8641':'Civic, Social, Fraternal Associations',
'8651':'Political Organizations',
'8675':'Automobile Associations',
'8699':'Membership Organizations',
'8734':'Testing Laboratories',
'8911':'Architectural/Surveying Services',
'8931':'Accounting/Bookkeeping Services',
'8999':'Professional Services',
'9211':'Court Costs, Including Alimony and Child Support - Courts of Law',
'9222':'Fines   Government Administrative Entities',
'9223':'Bail and Bond Payments',
'9311':'Tax Payments   Government Agencies',
'9399':'Government Services (Not Elsewhere Classified)',
'9402':'Postal Services   Government Only',
'9405':'U.S. Federal Government Agencies or Departments',
'9950':'Intra Company Purchases'
};

#5)Open CSV file for writing
# Overpayments with green transactions - green activity that doesn't trigger red flags

count=0
with open('CC.Transactions.csv','w') as f1:
	writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
	writer.writerow(['rownum']+['Account_Number']+['Merchant_Name']+['Merchant_Category_Over_Code']+['Merchant_Category_Over_Desc']+\
	['Post_Date'] +	['Transaction_Date'] + ['Transaction_Type'] +['Merchant_Country_Over']+['Credit_Limit']+['Amount']+['Balance'])
	#6)Create a loop for each account and generate account from the customer account_id file 
	for i in range(5):
			acct=random.choice(python_account_ID.accountid)
			#7)Set customer credit limit - skew to clients with $1000-$25000 and 10% with $25K - $50K
			limit = max(max((randrange(1,101,1)-99),0)* randrange(25000,50000,1000),randrange(1000,25000,1000))
			#local Amt variable to calculate customer total usage
			usedAmt = 0
			maxDate= datetime(0001,01,01) 
			NoTrans = randrange(30,50,1)
			#loop to generate NoTrans transactions per customer, we can add logic for probabilities of # transactions if neccessary random number generator to avoid the constant value
			for j in range(NoTrans):
				dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				#generate amount for current transaction with 33%-66% distribution on credits and debits
				tmpAmt = max((randrange(1,4,1)-2),0)* randrange(1,limit,100)*(-1)
				#if not credit then generate debit
				if tmpAmt == 0:
					tmpAmt = randrange(1,limit,100)
				#add current amount to client total account usage
				usedAmt = usedAmt + tmpAmt
				#pull value from dictionary for randomly selected merchant category 
				cat = random.choice(Merchant_Category_Green)
				tranType = ''
				#set transaction type based on amount
				if tmpAmt < 0:
					tranType = random.choice(Transaction_Type_Credits)
				else: 
					tranType = random.choice(Transaction_Type_Debits)
				#tranType random.choice(Transaction_Type)
				#append values to row list 
				row = [str(count)+'_'+dt] + [acct] + [gen_data.create_company_name()] 
				row.append(cat)
				row.append(All_Merchant_Cat[cat])
				#date posted
				date1 = gen_data.create_date(past=True)
				if date1 > maxDate:
					maxDate = date1
				#date of transaction a day later
				date2 = date1-timedelta(days=1)
				row.extend([date1, date2, tranType,random.choice(Country_Green),limit,tmpAmt,usedAmt])
				count = count + 1
				writer.writerow(row)
			#post generating all transactions, check account balance - if overpaid - refund $ and add a refun transaction 
			if usedAmt < limit * (-1):
				row = [str(count)+'_'+dt]+ [acct] + ['']+['']+['']
				date1temp=maxDate+timedelta(days=90)
				date2=date1temp-timedelta(days=1)
				row.extend([date1temp, date2, 'Refund','',limit,abs(limit-abs(usedAmt))*(-1),0])
				count = count + 1
				usedAmt = 0
				maxDate= datetime(0001,01,01)
				writer.writerow(row)	
				
	#Yellow Transactions are defined by Merchant Category, Transaction Types and Country_Yellow.
	#Merchant Category is divided into three risk categories
	#As a reference was used MCC (Merchant Category Codes)
	#Just like MCC - Transaction Types were divided by risk and their frequencies were distributed accordingly. 
	#Country_Yellow Risk is distrubuted in three categories from the US AML Risk Guide Table
	for i in range(25):
			acct=random.choice(python_account_ID.accountid)
			#7)Set customer credit limit - skew to clients with $1000-$25000 and 10% with $25K - $50K
			limit = max(max((randrange(1,101,1)-99),0)* randrange(25000,50000,1000),randrange(1000,25000,1000))
			#local Amt variable to calculate customer total usage
			usedAmt = 0
			maxDate= datetime(0001,01,01) 
			NoTrans = randrange(30,50,1)
			#loop to generate NoTrans transactions per customer, we can add logic for probabilities of # transactions if neccessary random number generator to avoid the constant value
			for j in range(NoTrans):
				dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				#generate amount for current transaction with 50%-50% distribution on credits and debits
				tmpAmt = max((randrange(1,3,1)-1),0)* randrange(1,limit,100)*(-1)
				#if not credit then generate debit
				if tmpAmt == 0:
					tmpAmt = randrange(1,limit,100)
				#add current amount to client total account usage
				usedAmt = usedAmt + tmpAmt
				#pull value from dictionary for randomly selected merchant category 
				cat = random.choice(Merchant_Category_Yellow)
				tranType = ''
				#set transaction type based on amount
				if tmpAmt < 0:
					tranType = random.choice(Transaction_Type_Credits)
				else: 
					tranType = random.choice(Transaction_Type_Debits)
				#tranType random.choice(Transaction_Type)
				#append values to row list 
				row = [str(count)+'_'+dt] + [acct] + [gen_data.create_company_name()] 
				row.append(cat)
				row.append(All_Merchant_Cat[cat])
				#date posted
				date1 = gen_data.create_date(past=True)
				if date1 > maxDate:
					maxDate = date1
				#date of transaction a day later
				date2 = date1-timedelta(days=1)
				row.extend([date1, date2, tranType,random.choice(Country_Yellow),limit,tmpAmt,usedAmt])
				count = count + 1
				writer.writerow(row)
			#post generating all transactions, check account balance - if overpaid - refund $ and add a refun transaction 
			if usedAmt < limit * (-1):
				row = [str(count)+'_'+dt]+ [acct] + ['']+['']+['']
				date1temp=maxDate+timedelta(days=90)
				date2=date1temp-timedelta(days=1)
				row.extend([date1temp, date2, 'Refund','',limit,abs(limit-abs(usedAmt))*(-1),0])
				count = count + 1
				usedAmt = 0
				maxDate= datetime(0001,01,01)
				writer.writerow(row)

	#Green Transactions are defined by Merchant Category, Transaction Types and Country_Green.
	#Merchant Category is divided into three risk categories As a reference we used MCC (Merchant Category Codes)
	#Just like MCC - Transaction Types were divided by risk and their frequencies were distributed accordingly. 
	#Country_Green Risk is distrubuted in three categories from the US AML Risk Guide Table 
	for i in range(400):
			acct=random.choice(python_account_ID.accountid)
			#7)Set customer credit limit - skew to clients with $1000-$25000 and 10% with $25K - $50K
			limit = max(max((randrange(1,101,1)-99),0)* randrange(25000,50000,1000),randrange(1000,25000,1000))
			#local Amt variable to calculate customer total usage
			usedAmt = 0
			maxDate= datetime(0001,01,01) 
			NoTrans = randrange(30,50,1)
			#loop to generate NoTrans transactions per customer, we can add logic for probabilities of # transactions if neccessary random number generator to avoid the constant value
			for j in range(NoTrans):
				dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				#generate amount for current transaction with 50%-50% distribution on credits and debits
				tmpAmt = max((randrange(1,3,1)-1),0)* randrange(1,limit,100)*(-1)
				#if not credit then generate debit
				if tmpAmt == 0:
					tmpAmt = randrange(1,limit,100)
				#add current amount to client total account usage
				usedAmt = usedAmt + tmpAmt
				#pull value from dictionary for randomly selected merchant category 
				cat = random.choice(Merchant_Category_Green)
				tranType = ''
				#set transaction type based on amount
				if tmpAmt < 0:
					tranType = random.choice(Transaction_Type_Credits)
				else: 
					tranType = random.choice(Transaction_Type_Debits)
				#tranType random.choice(Transaction_Type)
				#append values to row list 
				row = [str(count)+'_'+dt] + [acct] + [gen_data.create_company_name()] 
				row.append(cat)
				row.append(All_Merchant_Cat[cat])
				#date posted
				date1 = gen_data.create_date(past=True)
				if date1 > maxDate:
					maxDate = date1
				#date of transaction a day later
				date2 = date1-timedelta(days=1)
				row.extend([date1, date2, tranType,'US',limit,tmpAmt,usedAmt])
				count = count + 1
				writer.writerow(row)
			#post generating all transactions, check account balance - if overpaid - refund $ and add a refun transaction 
			if usedAmt < limit * (-1):
				row = [str(count)+'_'+dt]+ [acct] + ['']+['']+['']
				date1temp=maxDate+timedelta(days=90)
				date2=date1temp-timedelta(days=1)
				row.extend([date1temp, date2, 'Refund','',limit,abs(limit-abs(usedAmt))*(-1),0])
				count = count + 1
				usedAmt = 0
				maxDate= datetime(0001,01,01)
				writer.writerow(row)
	#Red Transactions are defined by Merchant Category, Transaction Types and Country_Red.
	#Merchant Category is divided into three risk categories per senor Kamin's best judgement. - % to be updated
	#As a reference was used MCC (Merchant Category Codes)
	#Just like MCC - Transaction Types were divided by risk and their frequencies were distributed accordingly. 
	#Country_Red Risk is distrubuted in three categories from the US AML Risk Guide Table 
	for i in range(5):
			acct=random.choice(python_account_ID.accountid)
			#7)Set customer credit limit - skew to clients with $1000-$25000 and 10% with $25K - $50K
			limit = max(max((randrange(1,101,1)-99),0)* randrange(25000,50000,1000),randrange(1000,25000,1000))
			#local Amt variable to calculate customer total usage
			usedAmt = 0
			maxDate= datetime(0001,01,01) 
			NoTrans = randrange(30,50,1)
			#loop to generate NoTrans transactions per customer, we can add logic for probabilities of # transactions if neccessary random number generator to avoid the constant value
			for j in range(NoTrans):
				dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				#generate amount for current transaction with 50%-50% distribution on credits and debits
				tmpAmt = max((randrange(1,3,1)-1),0)* randrange(1,limit,100)*(-1)
				#if not credit then generate debit
				if tmpAmt == 0:
					tmpAmt = randrange(1,limit,100)
				#add current amount to client total account usage
				usedAmt = usedAmt + tmpAmt
				#pull value from dictionary for randomly selected merchant category 
				cat = random.choice(Merchant_Category_Red)
				tranType = ''
				#set transaction type based on amount
				if tmpAmt < 0:
					tranType = random.choice(Transaction_Type_Credits)
				else: 
					tranType = random.choice(Transaction_Type_Debits)
				#tranType random.choice(Transaction_Type)
				#append values to row list 
				row = [str(count)+'_'+dt] + [acct] + [gen_data.create_company_name()] 
				row.append(cat)
				row.append(All_Merchant_Cat[cat])
				#date posted
				date1 = gen_data.create_date(past=True)
				if date1 > maxDate:
					maxDate = date1
				#date of transaction a day later
				date2 = date1-timedelta(days=1)
				row.extend([date1, date2, tranType,random.choice(Country_Red),limit,tmpAmt,usedAmt])
				count = count + 1
				writer.writerow(row)
			#post generating all transactions, check account balance - if overpaid - refund $ and add a refun transaction 
			if usedAmt < limit * (-1):
				row = [str(count)+'_'+dt]+ [acct] + ['']+['']+['']
				date1temp=maxDate+timedelta(days=90)
				date2=date1temp-timedelta(days=1)
				row.extend([date1temp, date2, 'Refund','',limit,abs(limit-abs(usedAmt))*(-1),0])
				count = count + 1
				usedAmt = 0
				maxDate= datetime(0001,01,01)
				writer.writerow(row)
	#Green Transactions with Merchant Credits - but no corresponding debits 
	for i in range(5):
			acct=random.choice(python_account_ID.accountid)
			#7)Set customer credit limit - skew to clients with $1000-$25000 and 10% with $25K - $50K
			limit = max(max((randrange(1,101,1)-99),0)* randrange(25000,50000,1000),randrange(1000,25000,1000))
			#local Amt variable to calculate customer total usage
			usedAmt = 0
			maxDate= datetime(0001,01,01) 
			NoTrans = randrange(30,50,1)
			#loop to generate NoTrans transactions per customer, we can add logic for probabilities of # transactions if neccessary random number generator to avoid the constant value
			for j in range(NoTrans):
				dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				#generate amount for current transaction with 50%-50% distribution on credits and debits
				#tmpAmt = max((randrange(1,3,1)-1),0)* randrange(1,limit,100)*(-1)
				#if not credit then generate debit
				#if tmpAmt == 0:
				tmpAmt = randrange(1,limit,100)
				#add current amount to client total account usage
				usedAmt = usedAmt + tmpAmt
				#pull value from dictionary for randomly selected merchant category 
				cat = random.choice(Merchant_Category_Green)
				tranType = ''
				#set transaction type based on amount		
				tranType = random.choice(Transaction_Type_Credits)
				#tranType random.choice(Transaction_Type)
				#append values to row list 
				row = [str(count)+'_'+dt] + [acct] + [gen_data.create_company_name()] 
				row.append(cat)
				row.append(All_Merchant_Cat[cat])
				#date posted
				date1 = gen_data.create_date(past=True)
				if date1 > maxDate:
					maxDate = date1
				#date of transaction a day later
				date2 = date1-timedelta(days=1)
				row.extend([date1, date2, tranType,'US',limit,tmpAmt,usedAmt])
				count = count + 1
				writer.writerow(row)
			#post generating all transactions, check account balance - if overpaid - refund $ and add a refun transaction 
			if usedAmt < limit * (-1):
				row = [str(count)+'_'+dt]+ [acct] + ['']+['']+['']
				date1temp=maxDate+timedelta(days=90)
				date2=date1temp-timedelta(days=1)
				row.extend([date1temp, date2, 'Refund','',limit,abs(limit-abs(usedAmt))*(-1),0])
				count = count + 1
				usedAmt = 0
				maxDate= datetime(0001,01,01)
				writer.writerow(row)
	#Red Transactions with payments from non BMO entities 
	for i in range(5):
			acct=random.choice(python_account_ID.accountid)
			#7)Set customer credit limit - skew to clients with $1000-$25000 and 10% with $25K - $50K
			limit = max(max((randrange(1,101,1)-99),0)* randrange(25000,50000,1000),randrange(1000,25000,1000))
			#local Amt variable to calculate customer total usage
			usedAmt = 0
			maxDate= datetime(0001,01,01) 
			NoTrans = randrange(30,50,1)
			#loop to generate NoTrans transactions per customer, we can add logic for probabilities of # transactions if neccessary random number generator to avoid the constant value
			for j in range(NoTrans):
				dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				#generate amount for current transaction with 50%-50% distribution on credits and debits
				tmpAmt = max((randrange(1,3,1)-1),0)* randrange(1,limit,100)*(-1)
				#if not credit then generate debit
				if tmpAmt == 0:
					tmpAmt = randrange(1,limit,100)
				#add current amount to client total account usage
				usedAmt = usedAmt + tmpAmt
				#pull value from dictionary for randomly selected merchant category 
				cat = ''
				tranType = ''
				#set transaction type based on amount
				if tmpAmt < 0:
					tranType = random.choice(Transaction_Type_Credits)
					cat='Non-BMO Acct'
				else: 
					tranType = random.choice(Transaction_Type_Debits)
				#tranType random.choice(Transaction_Type)
				#append values to row list 
				row = [str(count)+'_'+dt] + [acct] + [gen_data.create_company_name()] 
				row.append(cat)
				row.append('')
				#date posted
				date1 = gen_data.create_date(past=True)
				if date1 > maxDate:
					maxDate = date1
				#date of transaction a day later
				date2 = date1-timedelta(days=1)
				row.extend([date1, date2, tranType,random.choice(Country_Red),limit,tmpAmt,usedAmt])
				count = count + 1
				writer.writerow(row)
			#post generating all transactions, check account balance - if overpaid - refund $ and add a refun transaction 
			if usedAmt < limit * (-1):
				row = [str(count)+'_'+dt]+ [acct] + ['']+['']+['']
				date1temp=maxDate+timedelta(days=90)
				date2=date1temp-timedelta(days=1)
				row.extend([date1temp, date2, 'Refund','',limit,abs(limit-abs(usedAmt))*(-1),0])
				count = count + 1
				usedAmt = 0
				maxDate= datetime(0001,01,01)
				writer.writerow(row)
