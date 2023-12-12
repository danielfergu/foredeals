#from web_app.app import db
from data_collector.CollectList import CollectList

def test_parse():
    html_content = '''<html><body><table data-role="selectable" class="k-selectable" aria-colcount="6" tabindex="0" id="f74286a9-5ddb-40de-8014-39329fd0b077" aria-rowcount="78"><colgroup><col style="width:80px"><col><col style="width:105px"><col style="width:50px"></colgroup><thead role="rowgroup" class="k-grid-header"><tr role="row" aria-rowindex="1"><th scope="col" data-field="AuctionId" rowspan="1" data-title="ID" data-index="0" id="d70da35e-1e64-4032-bdba-f9ad0ff1068a" class="k-header" data-role="columnsorter" aria-colindex="1" role="columnheader"><span class="k-cell-inner"><span class="k-link"><span class="k-column-title">ID</span></span></span></th><th scope="col" data-field="ThumbnailImageUrl" rowspan="1" data-title="&nbsp;" data-index="1" id="a5355386-7624-47e9-be45-38df67532b58" class="k-header" data-role="columnsorter" aria-colindex="2" style="display: none;" role="columnheader"><span class="k-cell-inner"><span class="k-link"><span class="k-column-title">&nbsp;</span></span></span></th><th scope="col" data-field="AssetTitle" rowspan="1" data-title="Auction Title" data-index="2" id="fe30cc91-6c1e-46de-8f2e-797921021755" class="k-header" data-role="columnsorter" aria-colindex="3" role="columnheader"><span class="k-cell-inner"><span class="k-link"><span class="k-column-title">Auction Title</span></span></span></th><th scope="col" data-field="CurrentBid" rowspan="1" data-title="Current Bid" data-index="3" id="dfce3c92-c581-45c1-9e7e-4e93a7bf386a" class="k-header" data-role="columnsorter" aria-colindex="4" role="columnheader"><span class="k-cell-inner"><span class="k-link"><span class="k-column-title">Current Bid</span></span></span></th><th scope="col" data-field="BidCount" rowspan="1" data-title="# Bids" data-index="4" id="cfc0ba72-e52e-4e1d-b382-54ba55fc229f" class="k-header" data-role="columnsorter" aria-colindex="5" role="columnheader"><span class="k-cell-inner"><span class="k-link"><span class="k-column-title"># Bids</span></span></span></th><th scope="col" data-field="ActualCloseTime" rowspan="1" data-title="Closes" data-index="5" id="cef7cef5-2ba8-4ffa-9ff7-82753b44da5d" class="k-header" data-role="columnsorter" aria-colindex="6" style="display: none;" role="columnheader"><span class="k-cell-inner"><span class="k-link"><span class="k-column-title">Closes</span></span></span></th></tr></thead><tbody role="rowgroup"><tr class="k-master-row" data-uid="dbed6205-94de-4e2f-8055-592c8c8dc8c3" role="row" aria-rowindex="2">
<td role="gridcell">1120077</td>
<td style="display:none" role="gridcell"><img class="grid-thumbnail" src="https://b4apubresources.blob.core.windows.net/mainimages/MainImage_1120077_515e08e93519425993ac3ef0b32b3c72.jpg" width="84"></td><td role="gridcell">
    <div>
        Mobile Home Lot 3049 Square Foot  Property Modoc County, California        
            <br>
            <strong>CA, California Pines</strong>
    </div>
</td>

<td style="text-align: center;" role="gridcell"></td><td role="gridcell"></td><td style="display:none" role="gridcell"> 4h 22m </td></tr><tr class="k-alt k-master-row" data-uid="e7f2f679-c45d-4678-a4d9-ec4c1dc30a5b" role="row" aria-rowindex="3"><td role="gridcell">1120217</td><td style="display:none" role="gridcell"><img class="grid-thumbnail" src="https://b4apubresources.blob.core.windows.net/mainimages/MainImage_1067668_f86af344744446aebe1dc2e6a639bacc.jpg" width="84"></td><td role="gridcell">
    <div>
        Camp on Your Acre of Huge Pines in Peaceful California Pines, Modoc County, California - No Buyer's Premium! 
        
            <br>
            <strong>CA, Alturas</strong>
        
    </div>
</td>

<td style="text-align: center;" role="gridcell"></td><td role="gridcell"></td><td style="display:none" role="gridcell"> 12/11/2023<br>3:00 PM </td></tr><tr class="k-master-row" data-uid="f158cc5f-de53-4a24-93a9-4e6cb8c31f10" role="row" aria-rowindex="4"><td role="gridcell">1119200</td><td style="display:none" role="gridcell"><img class="grid-thumbnail" src="https://b4apubresources.blob.core.windows.net/mainimages/MainImage_1119200_a9d397fa06984fa6b7d694df9e454017.jpg" width="84"></td><td role="gridcell">
    <div>
        Welcome to Imperial County, California!  - No Buyer's Premium!
        
            <br>
            <strong>CA, Imperial</strong>
        
    </div>
</td>


<td style="text-align: center;" role="gridcell"></td><td role="gridcell"></td><td style="display:none" role="gridcell"> 12/11/2023<br>3:00 PM </td></tr></tbody></table></html></body>'''

    collector = CollectList()
    collector.parse(html_content)
    print(len(collector.parsed_data))
    assert collector.parsed_data[0]["city"] == "California Pines"


