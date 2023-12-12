#from web_app.app import db
from data_collector.CollectAuction import CollectAuction
import datetime

def test_parse():
    html_content = '''<div class="breadcrumbs">
    <a href="/real-estate-auctions">Real Estate</a> &gt; <a href="/bid-and-assume-auctions">Bid &amp; Assume</a> &gt; <a href="/channel/22-real-estate/02-bid-and-assume/00-all">All</a> &gt; <span style="font-size: 1.8em"># 1120090</span>
</div>
<h1 style="font-family: 'OpenSans-Regular';">
TX, Red River, 5.04 Acre Wishing Star Ranch, Lot 39.TERMS $522/Month</h1>

<div class="auction-left" id="auction-detail-left">


    <div class="tabs">

        <!-- - - - - - - - - - - - - - Tab - - - - - - - - - - - - - - - - - -->
        <div class="tab" id="tab1" style="min-height:340px;">
                <img src="https://publicresources.bid4assets.com/mainimages/MainImage_1120090_d304e1ae323f4287b371bd6a09afcf81_Resized.jpg" onload="mainImageLoaded(this)" id="mainImage" onerror="mainImageError()" style="width: 96%;">
        </div>
        <!-- - - - - - - - - - - - - - End of Tab - - - - - - - - - - - - - - - - -->
        <ul class="tabs_nav">
        </ul>
    </div><!-- end tabs -->

    <div class="auction-info-summary">

        <table>
            <tbody><tr>
                <td nowrap="nowrap"><strong>Seller Name:</strong></td>
                <td style="padding-left: 10px;"><a href="/v5/search/#t=s|s=131493|sc=bidclosetime|so=ASC">onlinelandsales</a></td>
            </tr>
            <tr>
                <td><strong>Rating:</strong></td>
                <td>
<span class="k-rating k-widget k-disabled" role="slider" aria-valuemin="1" aria-valuemax="5" aria-valuenow="4.0" aria-disabled="true" style=""><input id="sellerRating" name="sellerRating" type="text" value="4" data-role="rating" class="k-hidden" disabled="disabled"><span class="k-rating-container"><span class="k-rating-item k-selected" data-value="1" title="1"><span class="k-icon k-i-star"></span></span><span class="k-rating-item k-selected" data-value="2" title="2"><span class="k-icon k-i-star"></span></span><span class="k-rating-item k-selected" data-value="3" title="3"><span class="k-icon k-i-star"></span></span><span class="k-rating-item k-selected" data-value="4" title="4"><span class="k-rating-precision-complement" style="width: 0px; left: 0px;"><span class="k-icon k-i-star-outline"></span></span><span class="k-rating-precision-part" style="width: 24px;"><span class="k-icon k-i-star"></span></span><span style="width: 24px; height: 24px; display: block;"></span></span><span class="k-rating-item" data-value="5" title="5"><span class="k-icon k-i-star-outline"></span></span></span></span><script>kendo.syncReady(function(){jQuery("#sellerRating").kendoRating({"min":1,"max":5,"precision":"half","label":false,"enabled":false,"value":4});});</script>&nbsp; 
                            <a href="/myb4a/bidder/sellerfeedbacksummary/131493">(113)</a>
                </td>
            </tr>
            <tr>
                <td><strong>Location:</strong></td>
                <td style="padding-left: 10px;">
Annona, TX 75550                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <a href="http://www.addthis.com/bookmark.php?v=250&amp;pub=xa-4a43c24931dccd19" onmouseover="return addthis_open(this, '', '[URL]', '[TITLE]')" onmouseout="addthis_close()" onclick="return addthis_sendto()"><img src="https://secure.addthis.com/static/btn/lg-share-en.gif" width="125" height="16" alt="Bookmark and Share" style="border:0"></a>
<script type="text/javascript" src="https://secure.addthis.com/js/250/addthis_widget.js?pub=xa-4a43c24931dccd19"></script>
                </td>
            </tr>
        </tbody></table>

        <div class="clearfix"></div>

        <div class="share-auction">
            <p>Share</p>
            <div class="share-auction-icons">
                <a href="#"><div class="fa-facebook"></div></a>
                <a href="#"><div class="fa-twitter"></div></a>
                <a href="#"><div class="fa-google-plus"></div></a>
                <a href="#"><div class="fa-envelope"></div></a>
                <div class="clearfix"></div>
            </div><!-- end share-auction-icons -->
            <div class="clearfix"></div>
        </div><!-- end share-auction -->
    </div><!-- end auction-info-summary -->


</div><!-- end auction-left -->


<div class="auction-right" id="auction-right-panel">
        
    <div class="place-bid-box" style="margin-bottom: 5px;">
            <div class="current-bid">

                <h4>Current BID: <span id="current-bid-span">$1</span></h4>
                <p>
                    <a href="#" class="tooltip_container">
                        <span class="tooltip right">It is the minimum amount you can bid above the current bid price. A bidder can place a bid amount that is equal to or greater than the bid increment (e.g., through a flat bid using our advanced bidding features), just not less than the bid increment.</span>
                        <i>Bid Increment:</i>
                    </a>

                    <span>$1</span>
                </p>

            </div><!-- end current-bid -->
            <div class="your-bid">

                <label for="bid">Your BID:</label>
                <input style="margin-top: 5px; width: 150px;" type="text" id="bid" onfocus="bidInputFieldFocused = true;" onblur="bidInputFieldFocused=false; reformatBidValue()" required="" name="cf_bid" data-field-name="bid" data-min-characters="" value="$1" placeholder="$1">
                <div class="clearfix"></div>
                <p>
Enter US $1 or more                </p>
                <script type="text/javascript">
                    originalBidValue = '$1';
                    var isSealedBidAuction = false;
                    var currentMinBidAmount = 1;
                    function reformatBidValue() {
                        currentBidValue = parseInt(jQuery.trim($("#bid").val()).replace('$', '').replace(/,/g, ''), 10);
                        if (isNaN(currentBidValue)) {
                            $("#bid").val(originalBidValue);
                        } else {
                            if (isSealedBidAuction)
                            {
                                if (currentBidValue < currentMinBidAmount) {
                                    currentBidValue = currentMinBidAmount;
                                }
                            }
                            $("#bid").val("$" + currentBidValue);
                        }
                    }
                </script>
            </div><!-- end your-bid -->
                <button id="bid-button" onclick="placeBid(false)">Place bid</button>


        <div class="clearfix"></div>
    </div><!-- end place-bid-box -->


            <h3>This is a NO RESERVE auction</h3>

    <h5 id="autoupdate-description-block">Auto <a href="javascript:void(0)" onclick="reloadAuctionRightPanel(true)">update</a> in <span id="auction-refresh-countdown">1 hour</span></h5>
<div class="clearfix"></div>


<div class="auction-data-table">
        <table>
                <tbody><tr>
                    <th>Number of Bids:</th>
                    <td id="num-bids-block">0</td>
                </tr>
                <tr>
                    <th>
                        <a href="#" class="tooltip_container">
                            <span class="tooltip right">
                                It is the floor at which bidding begins. Our system cannot accept a bid lower than the minimum bid amount.
                            </span>
                            <i>Minimum Bid:</i>
                        </a>
                    </th>
                        <td>$1</td>
                </tr>
                <tr>
                    <th>Closes In:</th>
                    <td id="time-remaining-block">
                        <b>4 <i>hr</i></b>
                    </td>
                </tr>
            <tr>
                <th>Your Bid Status:</th>
                    <td><a href="/myaccount/login?ReturnUrl=%2fauction%2fdetail%2f1120090">Log in</a> to view status</td>
            </tr>
                <tr>
                    <th>
                        <a href="#" class="tooltip_container">
                            <span class="tooltip right">It is the minimum dollar amount a Seller is willing to accept for an auction. This amount is not disclosed on the Web site, but bidders are notified once the reserve price has been met. Auctions with no reserve price are labeled as "No Reserve" on the auction listing.</span>
                            <i> Reserve:</i>
                        </a>
                    </th>
                    <td>
                            <strong>No Reserve!</strong>
                    </td>
                </tr>
                <tr>
                    <th>Status:</th>
                    <td>In Progress</td>
                </tr>
                <tr>
                    <th>Auction Started:</th>
                    <td>12-04-23 12:15 PM ET</td>
                </tr>
                <tr>
                    <th>Auction Closes:</th>
                    <td>
                        <span id="actual-close-time-block">
                            12-11-23 12:15 PM ET
                        </span>
                        <img alt="Overtime Image!" src="https://cdn.bid4assets.com/static/overtime.gif" border="0" id="overtime-image" style="display:none;">
                    </td>
                </tr>
                    <tr>
                        <th>
                            <a href="#" class="tooltip_container">
                                <span class="tooltip right">It is an extension of the auction close time and keeps an auction open as long as there is active bidding. It occurs automatically when a bid is placed within the last few minutes of an auction. The auction will remain open until an entire overtime increment has passed without any bidding. The overtime increment is indicated on the auction listing.</span>
                                <i>Overtime Period:</i>
                            </a>
                        </th>
                        <td>
                            5 minutes
                        </td>
                    </tr>
            <tr>
                <th>Source:</th>
                <td>Private Auction</td>
            </tr>
            <tr>
                <th>Deposit Required:</th>
                <td>
$0                </td>
            </tr>
            <tr>
                <th>Page Views:</th>
                <td id="auction-detail-page-views">289</td>
            </tr>

        </tbody></table>

</div><!-- end auction-data-table -->

'''

    collector = CollectAuction()
    collector.parse(html_content)
    assert collector.parsed_data[0]["auid"] == 1120090
    assert collector.parsed_data[0]["sqft"] == 174240
    assert collector.parsed_data[0]["price"] == 1
    assert collector.parsed_data[0]["zip_code"] == 75550
    assert collector.parsed_data[0]["date_start"] == datetime.datetime(2023, 12, 4, 12, 15)
    assert collector.parsed_data[0]["date_end"] == datetime.datetime(2023, 12, 11, 12, 15)

