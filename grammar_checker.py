import g4f, asyncio
from keys import prompt, gpt_access_token

prompt = """
Merhaba,
sana bir tweet verdiğimde aşağıdaki formatta tweet hazırlamanı istiyorum:

Merhaba!\n
"{komik yorum}\n
{ek kontrolü}"

komik yorum: tweet içeriği ve sahibi hakkında komik bir yorum ile cevabına başla,
ek kontrolü: tweet içindeki dahi anlamındaki -de/ -da ekinin doğruluğunu kontrol et.

emoji SAKIN KULLANMA

Örneğin sana "aynen kanka rengarenk kisiligim var benimde" tweetini verdiğimde senin cevabın şöyle olmalı:
Merhaba!\n
Aynen kanka, ne kadar renkli gerçekten.

Yalnız tweetteki "benimde" keilmesindeki "-de" eki ayrı yazılmalıydı.

"""

soru = "sende çok oldun"

cevap = """
Merhaba!

Sanırım çok oldum.

Ancak hatırlatmak isterim ki, "sende" kelimesindeki "-de" eki ayrı yazılmalıydı.
"""

soru2 = "benide çağırsanıza olm niye haber vermiyosunuz"

cevap2 = """Merhaba!

Tabii ki, seni çağırmak için buradayım. 

Yalnızca bir küçük not: Tweetindeki "benide" kelimesindeki "-de" eki ayrı yazılmalıydı. """



def ready_messages(message):
    return [{"role": "user", "content": prompt},
            {"role": "user", "content": soru},
            {"role": "assistant", "content": cevap},
            {"role": "user", "content": soru2},
            {"role": "assistant", "content": cevap2},
            {"role": "user", "content": message}]

def check_de(message):
# normal response
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=ready_messages(message),
        auth=True
    )  
    return response


# print(check_de("Hande Erçeli eleştirenlere bugüne kadar hiç cevap vermedim ama artık bende bir şeyler söylemek istiyorum cünkü benimde canıma tak etti artık! Hande’nin oyunculuğuna laf edenler haddinizi bilin! Hande Erçel dünya çapında tanınmış muazzam bir oyuncudur! Kimseye laf etmek düşmez!"))




