"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
"""


class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        return self._palindrome_pairs_less_brute(words)

    def _palindrome_pairs_brute(self, words):
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and self._is_palindrome_brute(words[i], words[j]):
                    result.append([i, j])
        return result

    def _palindrome_pairs_less_brute(self, words):
        result = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and self._is_palindrome(words[i], words[j]):
                    result.append([i, j])
        return result

    def _is_palindrome(self, word1, word2):
        # print("checking: ", word1, word2)
        l1 = len(word1)
        l2 = len(word2)
        for i in range((l1 + l2) // 2):
            if i < l1 and i < l2:
                let1 = word1[i]
                let2 = word2[l2 - 1 - i]
            elif i >= l1:
                let1 = word2[i - l1]
                let2 = word2[l2 - 1 - i]
            else:
                let1 = word1[i]
                let2 = word1[l1 - 1 - (i - l2)]
            if let1 != let2:
                return False
        return True

    def _is_palindrome_brute(self, word1, word2):
        word = word1 + word2
        l = len(word)
        for i in range(l // 2):
            let1 = word[i]
            let2 = word[l - 1 - i]
            if let1 != let2:
                return False
        return True


if __name__ == '__main__':
    tests = [
        # ["abcd", "dcba", "lls", "s", "sssll"],
        # ["bat", "tab", "cat"],
        ["hiaeejjifdjjfichad", "bgjj", "f", "h", "dfedeggdeiagedgffb", "dcijiadgheaaggeddcb", "a", "dfhb", "fa", "bc",
         "gcdbed", "gfd", "ifhibc", "icdca", "dddedj", "ejiajedefj", "diaeahgiijhga", "aaa", "fefihjaf",
         "ajbchccdhcdefe", "jc", "gghei", "ifed", "jabbibh", "aghddfdcadfa", "dejbibgj", "aggaggffdefbeacjj",
         "idijgbdjfbgi", "icgfdbebfgfajafcg", "jfgcgeh", "agbdb", "agfej", "gjebebjhghhicbibd", "je", "fjgddi",
         "cfgjcjbbgijiciccfiha", "gehfiiahgecaiefceic", "hfdhihbdj", "dhahadfcghdffjhdh", "eijjecadeicffheghgh",
         "bbfjfghghciigejibj", "gdjbecjfhfgjc", "jhf", "jfhghgeaagaeefhbi", "jbdjahhdadfcbaihja", "egeafiihh",
         "bghdefjhbchgiegbcd", "edechjfdbjhiabc", "jdjcccaciacide", "fdfihehgdcdcjaeajd", "ebdfdchgj", "faih", "jhbd",
         "gbgbgbid", "caagbbfgccib", "feebfgfjja", "bgcjdiadi", "bcdfeabdhfjec", "hebjehddihcbicaf",
         "fjbjgdjacfbabgcfjchh", "ccfhjfgacafjaf", "cddfhjdebdgff", "cafedechigjc", "hecebacjgcf", "gecgfgeeaachhjb",
         "jdjceedhecbccdggbhb", "ciihcfca", "jbadfgaicgeefhciab", "idbeedfhfebiabdahad", "icigjaifc", "hcighg", "hh",
         "igiceae", "ecfdcijh", "hj", "j", "cfcghbhjbgfijefbajd", "hhdhghbifaj", "ihbicgaj", "fb",
         "jidghfbaaejegaiebcf", "eifhjdhghjegdhcjefj", "efdjae", "gbahiagbhbjgg", "cibigeijfciafgegdfc",
         "jafijegfbhhcejcg", "adadaej", "ajeadhjdhhjjefdbeiff", "jgiecchcgbcfdchd", "ijgdgaahdadfaddif", "eddfhajb",
         "fhb", "hebfgegci", "aifdade", "ajbhjbecdjhjccah", "bcehijbhcggbeedffec", "deigedegbi", "difdhbfbibi", "c",
         "gjehafbjfadjgfacce", "ifgcgahehchajdiadihg", "bb", "iee", "biiidbebjhfefbjjhih", "bdjgcjfe",
         "hbdfbhihcffaabhe", "hehfgbfjbifcbjab", "cbgjheebajheiccdde", "bh", "ifegagaaaidbhchcf", "fbgjgcfbi",
         "abfiajdfbbjhee", "gcf", "iaaabhbieidjhi", "e", "ged", "ech", "jchjebagachhchdfcj", "jfebidb", "ecie", "fg",
         "jijjcjaehcbchgib", "dgjebjaifejiiidfge", "dfacjecghjjiicbj", "eecgeidiiiaggghi", "jbechfica",
         "dfdiffibgigjij", "hajejhjdijacea", "fadfdjcbjfh", "heigeecajc", "fhde", "ijh", "adhcajghdcdbfdd",
         "gjfcbaaebghe", "gdhdihefbhebcad", "fdejcabaficdjbi", "iigjeif", "ejhbjecebdgiiedbe", "ghfadffjhjffj",
         "faedjcejecgifbja", "igjaidcjghegji", "ijgeccajiaabg", "cjigeeddbbbfcibfbgf", "habfeiajajbgdce", "ajgaifi",
         "afddh", "bbbabccgecfgdeebiceg", "jafdaehiecbcgg", "ceeifejcg", "bahacfhdihhdfjihij", "hbgbbhidfecc",
         "fbcacaahjehhbijbf", "jbbhiegidihbdjgic", "fhhcfjgeijbbfjigeb", "bijhfhhhjjgibibbbihb", "haaaiddib", "die",
         "bje", "ejfjgceicibibacdea", "egbeai", "cbgicecgcffg", "dbehcgffadgcd", "bfddgfbihafdfbh", "adidicjdjhdb",
         "gh", "fdaaahbjbge", "cggdibhejiiidfdciecd", "cabjbidc", "hcecahggjeiadgih", "cgefaddfci", "bgehicceaiabc",
         "bfejchbhdfecjgddigeh", "aehfebigheddd", "caifjid", "ajbac", "i", "cajbagaccjghifhicgeh", "aaiaiaedbaffcifj",
         "hjeciiic", "fcjdjhiaadehchjcj", "ichj", "efbjibed", "gba", "eejdgjbhccbcibcij", "d", "haja", "hbcdciggg",
         "jcdffaj", "efeaidbafhgbaehci", "ahfjebdidcghahe", "caaaahg", "ahddbfccaed", "ghaaieaji", "bjih",
         "edhcdheejdbehbhdjif", "aiighdgejehdfcad", "gdhijb", "fggbcaeeeiehhabbiai", "eajgcjeajai", "eaheecdbaaagbedga",
         "bbdehcgdfidigjhcge", "acdhhc", "hhjhjhcae", "jiggabhiigj", "cd", "cegd", "gejacegegejcabdhdjf", "bdhffgf",
         "ejggjhegifahhjbde", "eb", "dbagibhfgfgfhb", "dafjideje", "bgejcjiebigj", "dih", "agibha", "dbej", "fgffjff",
         "geeigjigfiijj", "eadaecbfihacb", "ebj", "aibcagfg", "ebeaccjeec", "ghidebgej", "dfigcfbbfedga", "faffbeifhb",
         "gbh", "eiigiebieadgdfgh", "fdabbghcjgeie", "djcbbfgeaa", "bjjefdagbgddjhdiehhg", "hhfjcbdachcieechfij",
         "agjahjee", "hhjgajfaeicgidgij", "deaaefac", "ddhcjeg", "fhbjbjdhbgjficij", "ehgaabjegehhagdgj",
         "cejbahfafdbiegb", "iebbigbcdcfbccibe", "afaajcgigeaehjebd", "ahdfgjeej", "ibahei", "ihegicd", "hijiijbeheiec",
         "efffh", "ccibhbijbifeab", "egdfdf", "ajjchbaiabfha", "edcjij", "fjhhhhgegj", "cfhccbhgjdebfdja", "cgfgej",
         "jfebdgaeaggcgagdaij", "dfefdagcaehcdfhggef", "ceh", "ggcihgefbebac", "bffgfhddgjajdgaiihge",
         "hhjcbjacfjjjdcfhegd", "hiaijfebghadgeibac", "eafhjghcbacbb", "hgdbhea", "gcia", "hdgfcbeehahddec",
         "bggaaihigbabdahgd", "cbifadddbaceibcjfj", "fjjedad", "g", "cadh", "eaibeeiaf", "ieechahcj", "ibagjagdj",
         "cijcbbbbffabaiiajjej", "cgfheihdjciigjced", "ggjchcedhbbjf", "cbccigbahfbidifjcb", "ejfebjhdiiha", "eefec",
         "geicajj", "ighjghjaaddgecdeci", "ccefibhjjf", "ieihfdbedbcdf", "fajigigbajgi", "ihihdicahfdgdbiaceh",
         "ffiigibggafdde", "iceddhjighbeeejihad", "iai", "hjihdida", "ecbaccffddd", "fbddhjde", "hgfhibahfejfdjhffed",
         "jahdcjecicbgbbg", "gc", "caafcaehjj", "iagafedghhbjhg", "dbfjheeafgadjf", "gfifjidiac", "ccehfcaieegiaeff",
         "eijhijffafbici", "ffdbfdeicdjagc", "hea", "abaeg", "bhe", "gcbj", "b", "jiiidbhfgjbebchdff",
         "cbfijcjajchjcififc", "ejdddgfdcajjcaifhg", "hhhdfahjfdcgfdb", "chb", "iccbacbgdeihddgb", "fhc", "jdccdbe",
         "fdfdjcjiiijjid", "chfcbdihffcbdda", "cihhgdacfidbcfeajed", "eaifgb", "geeahdfhaa", "daijjcjahfgadi",
         "jjedajedbbbjidie", "ghhbjbcicgafe", "daje", "fe", "giab", "dafhchdjcegffcg", "gjb", "cgicdff",
         "ddaaffdgbehhjfjjdb", "fehjbebbfdeababicc", "bjaffbaf", "bfd", "ifjdbbdjfjfifdaaeji", "cidadh",
         "ceegbffaaehgb", "ebcieidcdb", "gdahfcebijc", "jdaegechh", "iiccdgghega", "bdbjfhbjadjdhcefah", "eicdiajeif",
         "bifeiabdddhafedjhfbh", "ddjjejgiaejb", "dahgcejihgdc", "dbiedfcdigceabb", "ij", "eiefi", "acicigedjddegi",
         "adacfdeefdgicjbiigg", "ggghccbjidch", "cghigbbcfjh", "egddej", "ebdgcgjcjgfigdffged", "bcgebjedafbiahhahdbf",
         "aiagjggidd", "ajcgfahecdegadec", "dghiajaahbfbbjdjedda", "ca", "jjdjefij", "fbhcjeigbcfabe",
         "hhdidiehfcehedef", "cfafhjcigdafjhjbggb", "aa", "jejfigij", "dbdgcacejiihfehcc", "ebijhca", "jehgg", "ihd",
         "fd", "iagaiajie", "ahdfghecefagdagcig", "efidhjfbbegcgjedafh", "ehicccdfhfij", "hecffbfedijfefjjjgc",
         "cadfdfie", "eeg", "eaafgchifggajhdhbfjh", "haeg", "ehcehadicba", "gajafiehfjd", "cidbchcbhjicaafh",
         "dbdeaaaiciaidagc", "hbd", "bghhjaddcgdfghgia", "fgeddgjbhgfaabhghjhj", "cjgahgiccjaabecd", "hed",
         "hecjaaffigj", "bcafiec", "daf", "acbagicecifbbjgabig", "cibg", "jdbjdbb", "chhc", "hbdcjecfb", "jhcbijjaiid",
         "cfijbfdjhaddbjbjdeg", "idcjifd", "bfhc", "jdfacfacejccifaea", "hbbgjffgded", "jj", "ehdabfbjbhga",
         "fajcgedebcb", "hfgjbgeiabacbcd", "fj", "cfdihdcaj", "ggiggbbhjcfjejcii", "bggidi", "fifgajijghcigjedfaad",
         "bghcfae", "aefjifjfi", "biecgj", "aafddd", "hidiiadbafhaefhigii", "eigfbjgeidg", "cggcidigjjjgcfajdgh",
         "fceecgebfecafjahbaag", "ihafgabaa", "iieg", "ajffjbef", "bdafbbiicgfcadbf", "fbiajda", "geadiifccfdgcbfddade",
         "ffe", "adjjgaibfdhgjbgddc", "jf", "jhfegffea", "cedagjhiidjgcchhi", "hfcfebdeichegbaeih", "haahfaiebaadaiaci",
         "cjibaad", "gahfadigfbgjjbiiedd", "egggdcffdb", "iahcgjfhhgfgdde", "ddgffhab", "hijibcg", "gfaiei",
         "gcbgifbhbedbhdhhgf", "hbbabbf", "jjagec", "faacdjgaj", "geabi", "acgchgjfbhah", "hbbcbjjficfeiiejed",
         "faadghcf", "egfaabegaadd", "hfhbgjefcj", "dbiehebibdfjedbgj", "fdi", "bddbebcdacchdb", "cjjfdeaajjci"]
    ]
    s = Solution()
    for test in tests:
        print(s.palindromePairs(test))