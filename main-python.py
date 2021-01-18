#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import matplotlib.pyplot as plt
import os

veri_seti = pd.read_csv('olcum.txt') # txt dosyamızı csv formatında verisetimize ne kaydediyoruz.
veri_seti.to_csv('olcum.csv',index=None) # veri setimizi csv dosya formatında proje konumuna kaydediyoruz.
os.remove('olcum.txt') # txt dosyası ile işimiz kalmadı silebiliriz.
veri_seti.columns=['Sicaklik'] # sıcaklık değerlerini 'Sicaklik' kolon adı altında topluyoruz
veri_seti['OlcumNumarasi'] = [i for i in range(1,veri_seti.shape[0]+1)] # her sıcaklığın ölçü numarasını 'OlcumNumarasi' adlı kolonda tanımlıyoruz

plt.figure(figsize=(20,8)) # görsel panelin boyutu(width,height)
plt.plot(veri_seti.OlcumNumarasi,veri_seti.Sicaklik,color='red',linewidth=1,label='Sıcaklık Değişim')
plt.xlabel('Ölçüm Numarası')
plt.ylabel('Sıcaklık(Celsius)')
plt.legend()
plt.title('Oda Sıcaklığının Gün İçindeki Değişiminin Görsel Olarak Analiz Edilmesi')
plt.show()

