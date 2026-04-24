# Protocol Layer State Summaries

The [USB PD] Specification defines several Protocol Layer state machines that are designed to operate in parallel.
In USB Power Delivery Revision 3.0 some state machines were added and others had their functionality merged into existing state machines and removed.
The following table shows which state machines apply to each revision of the [USB PD] Specification:

| State Machine             | USB PD 2.0    | USB PD 3.0    |
| :-----------------------: | :-----------: | :-----------: |
| Protocol Layer Rx         | Yes           | Yes           |
| Protocol Layer Tx         | Yes           | Yes           |
| Hard Reset Operation      | Yes           | Yes           |
| BIST Rx Test              | Yes           | No            |
| BIST Tx Test              | Yes           | No            |
| Chunked Rx                | No            | Yes           |
| Chunked Tx                | No            | Yes           |
| Chunked Message Router    | No            | Yes           |

## Protocol Layer Rx

!!! quote ""
    ```mermaid
    stateDiagram-v2
        classDef onEntry stroke-width:0px;

        wait_for_phy_message : <a href="./rx-wait-for-phy-message">Rx.WaitForPHYMessage</a>
        check_message_type : <a href="./rx-check-message-type">Rx.CheckMessageType</a>
        layer_reset_for_receive : <a href="./rx-layer-reset-for-receive">Rx.LayerResetForReceive</a>
        check_message_id : <a href="./rx-check-message-id">Rx.CheckMessageID</a>
        store_message_id : <a href="./rx-store-message-id">Rx.StoreMessageID</a>

        %% >>> Configure States <<< %%

        state wait_for_phy_message {
            state "<b><u>Actions on Entry</u>:</b><br>- None" as wait_for_phy_message_entry
        }
        state check_message_type {
            state "<b><u>Actions on Entry</u>:</b><br>- Check message type<br>- Read <a href="../../../port-controller/registers/receive-buffer/#readable_byte_count">RECEIVE_BYTE_COUNT</a> and the<br>&nbsp;&nbsp;number of bytes it indicates<br>- Clear <a href="../../../port-controller/registers/alert/#received-sop-message-status">ALERT.RxStatus</a>" as check_message_type_entry
        }
        state layer_reset_for_receive {
            state "<b><u>Actions on Entry</u>:</b><br>- Reset MessageIDCounter<br>- Clear stored MessageID<br>- Protocol Layer Tx transitions to<br>&nbsp;&nbsp;<a href="./tx-phy-layer-reset">Tx.PHYLayerReset</a> state" as layer_reset_for_receive_entry
        }
        state check_message_id {
            state "<b><u>Actions on Entry</u>:</b><br>- Compare MessageID against<br>&nbsp;&nbsp;Stored MessageID" as check_message_id_entry
        }
        state store_message_id {
            state "<b><u>Actions on Entry</u>:</b><br>- Protocol Layer Tx transitions to<br>&nbsp;&nbsp;<a href="./tx-discard-message">Tx.DiscardMessage</a> state<br>- Store new Message ID<br>- Pass Message to Policy Engine" as store_message_id_entry
        }

        %% >>> Configure State Transitions <<< %%

        Startup --> wait_for_phy_message
        [*] --> wait_for_phy_message : Soft Reset request from<br>Policy Engine or<br>Exit from Hard Reset

        wait_for_phy_message --> check_message_type : <a href="../../../port-controller/registers/alert/#received-sop-message-status">ALERT.RxStatus</a>

        check_message_type --> [*] : Cable Reset<small><sup><a class="footnote-ref" href="#rx#colon;fn#colon;1">1</a></sup></small><br>Received
        check_message_type --> layer_reset_for_receive : Soft Reset<br>Received
        check_message_type --> check_message_id : Other Message<br>Received

        layer_reset_for_receive --> check_message_id : Soft Reset Complete

        check_message_id --> wait_for_phy_message : MessageID matches<br>Stored MessageID
        check_message_id --> store_message_id : MessageID does not match<br>Stored MessageID or<br>No MessageID Stored

        store_message_id --> wait_for_phy_message : Message passed to<br>Policy Engine

        class wait_for_phy_message_entry,check_message_type_entry,layer_reset_for_receive_entry,check_message_id_entry,store_message_id_entry onEntry
    ```
    { data-search-exclude }

    ***

    <div class="footnote">
      <ol>
          <li id="rx:fn:1">
            <p>A Cable Reset is detected when <a href="../../../port-controller/registers/alert/#received-sop-message-status">ALERT.RxStatus</a> is asserted and <a href="../../../port-controller/registers/receive-buffer/#received-sop-message">RX_BUF_FRAME_TYPE.RxMessage</a>=<code>110b</code></p>
          </li>
      </ol>
    </div>


## Protocol Layer Tx

!!! quote ""
    ```mermaid
    stateDiagram-v2
        classDef onEntry stroke-width:0px;

        discard_message : <a href="./tx-discard-message">Tx.DiscardMessage</a>
        phy_layer_reset : <a href="./tx-phy-layer-reset">Tx.PHYLayerReset</a>
        wait_for_message_request : <a href="./tx-wait-for-message-request">Tx.WaitForMessageRequest</a>
        layer_reset_for_transmit : <a href="./tx-layer-reset-for-transmit">Tx.LayerResetForTransmit</a>
        construct_message : <a href="./tx-construct-message">Tx.ConstructMessage</a>
        message_discarded : <a href="./tx-message-discarded">Tx.MessageDiscarded</a>
        transmission_error : <a href="./tx-transmission-error">Tx.TransmissionError</a>
        message_successful : <a href="./tx-message-successful">Tx.MessageSuccessful</a>

        %% >>> Configure States <<< %%

        state discard_message {
            state "<b><u>Actions on Entry</u>:</b><br>- Discard any message awaiting transmission<br>- Increment MessageID Counter" as discard_message_entry
        }
        state phy_layer_reset {
            state "<b><u>Actions on Entry</u>:</b><br>- None" as phy_layer_reset_entry
        }
        state wait_for_message_request {
            state "<b><u>Actions on Entry</u>:</b><br>- None" as wait_for_message_request_entry
        }
        state layer_reset_for_transmit {
            state "<b><u>Actions on Entry</u>:</b><br>- Reset MessageID Counter<br>- Protocol Layer Rx transitions to<br>&nbsp;&nbsp;<a href="./rx-wait-for-phy-message">Rx.WaitForPHYMessage</a> state" as layer_reset_for_transmit_entry
        }
        state construct_message {
            state "<b><u>Actions on Entry</u>:</b><br>- Write <a href="../../../port-controller/registers/transmit/#transmit">TRANSMIT</a> register" as construct_message_entry
        }
        state message_discarded {
            state "<b><u>Actions on Entry</u>:</b><br>- Clear <a href="../../../port-controller/registers/alert/#transmit-sop-message-discarded">ALERT.TxMessageDiscarded</a><br>- Start Retransmit timer (1ms)" as message_discarded_entry
        }
        state transmission_error {
            state "<b><u>Actions on Entry</u>:</b><br>- Increment MessageID Counter<br>- Inform Policy Engine of<br>&nbsp;&nbsp;Transmission Error<br>- Clear <a href="../../../port-controller/registers/alert/#transmit-sop-message-failed">ALERT.TxMessageFailed</a>" as transmission_error_entry
        }
        state message_successful {
            state "<b><u>Actions on Entry</u>:</b><br>- Increment MessageID Counter<br>- Inform Policy Engine<br>&nbsp;&nbsp;Message Sent<br>- Clear <a href="../../../port-controller/registers/alert/#transmit-sop-message-successful">ALERT.TxMessageSuccessful</a>" as message_successful_entry
        }

        %% >>> Configure State Transitions <<< %%

        Startup --> phy_layer_reset
        [*] --> phy_layer_reset : Exit from Hard Reset,<br>or Protocol Layer Rx entered<br><a href="./rx-layer-reset-for-receive">Rx.LayerResetForReceive</a> state
        [*] --> discard_message : Protocol Layer Rx entered<br><a href="./rx-store-message-id">Rx.StoreMessageID</a> state,<br>Fast Role Swap signal transmitted,<br>or Fast Role Swap signal detected

        discard_message --> phy_layer_reset : Discarding Complete

        phy_layer_reset --> wait_for_message_request : PHY Layer Reset Complete

        wait_for_message_request --> layer_reset_for_transmit : Received Soft Reset<br>Message Request
        wait_for_message_request --> construct_message : Received Other<br>Message Request
        
        layer_reset_for_transmit --> construct_message : PRL Layer Reset Complete

        construct_message --> message_successful : <a href="../../../port-controller/registers/alert/#transmit-sop-message-successful">ALERT.TxMessageSuccessful</a>
        construct_message --> message_discarded : <a href="../../../port-controller/registers/alert/#transmit-sop-message-discarded">ALERT.TxMessageDiscarded</a>
        construct_message --> transmission_error : <a href="../../../port-controller/registers/alert/#transmit-sop-message-failed">ALERT.TxMessageFailed</a>

        message_discarded --> construct_message : Retransmit<br>Timer Expires
        message_discarded --> wait_for_message_request : <a href="../../../port-controller/registers/alert/#received-sop-message-status">ALERT.RxStatus</a>

        transmission_error --> wait_for_message_request : Policy Engine informed<br>of Transmission Error

        message_successful --> wait_for_message_request : Policy Engine informed<br>Message Sent

        class discard_message_entry,phy_layer_reset_entry,wait_for_message_request_entry,layer_reset_for_transmit_entry,construct_message_entry,message_discarded_entry,transmission_error_entry,message_successful_entry onEntry
    ```
    { data-search-exclude }

## Hard Reset Operation

!!! quote ""
    ```mermaid
    stateDiagram-v2
        classDef onEntry stroke-width:0px;

        reset_layer : <a href="./hr-reset-layer">HR.ResetLayer</a>
        indicate_hard_reset : <a href="./hr-indicate-hard-reset">HR.IndicateHardReset</a>
        request_hard_reset : <a href="./hr-request-hard-reset">HR.RequestHardReset</a>
        wait_for_phy_hard_reset_complete : <a href="./hr-wait-for-phy-hard-reset-complete">HR.WaitForPHYHardResetComplete</a>
        phy_hard_reset_requested : <a href="./hr-phy-hard-reset-requested">HR.PHYHardResetRequested</a>
        wait_for_pe_hard_reset_complete : <a href="./hr-wait-for-pe-hard-reset-complete">HR.WaitForPEHardResetComplete</a>
        pe_hard_reset_complete : <a href="./hr-pe-hard-reset-complete">HR.PEHardResetComplete</a>

        %% >>> Configure States <<< %%

        state reset_layer {
            state "<b><u>Actions on Entry</u>:</b><br>- Reset MessageIDCounter" as reset_layer_entry
        }
        state indicate_hard_reset {
            state "<b><u>Actions on Entry</u>:</b><br>- Inform the Policy Engine of the<br>&nbsp;&nbsp;Hard Reset or Cable Reset" as indicate_hard_reset_entry
        }
        state request_hard_reset {
            state "<b><u>Actions on Entry</u>:</b><br>- Request PHY Layer to send<br>&nbsp;&nbsp;Hard Reset or Cable Reset<br>&nbsp;&nbsp;(write to <a href="../../../port-controller/registers/transmit/#transmit">TRANSMIT</a> register)" as request_hard_reset_entry
        }
        state wait_for_phy_hard_reset_complete {
            state "<b><u>Actions on Entry</u>:</b><br>- Wait for Hard Reset or Cable Reset<br>&nbsp;&nbsp;complete indication from PHY" as wait_for_phy_hard_reset_complete_entry
        }
        state phy_hard_reset_requested {
            state "<b><u>Actions on Entry</u>:</b><br>- Inform Policy Engine that Hard Reset<br>&nbsp;&nbsp;or Cable Reset Request has been sent" as phy_hard_reset_requested_entry
        }
        state wait_for_pe_hard_reset_complete {
            state "<b><u>Actions on Entry</u>:</b><br>- Wait for Hard Reset or Cable Reset<br>&nbsp;&nbsp;complete indication from PE" as wait_for_pe_hard_reset_complete_entry
        }
        state pe_hard_reset_complete {
            state "<b><u>Actions on Entry</u>:</b><br>- Inform PHY that Hard Reset is complete<br>&nbsp;&nbsp;by clearing all related alerts:<br>&nbsp;&nbsp;&nbsp;&nbsp;- <a href="../../../port-controller/registers/alert/#received-hard-reset">ALERT.HardReset</a><br>&nbsp;&nbsp;&nbsp;&nbsp;- <a href="../../../port-controller/registers/alert/#received-sop-message-status">ALERT.RxStatus</a><br>&nbsp;&nbsp;&nbsp;&nbsp;- <a href="../../../port-controller/registers/alert/#receive-buffer-overflow">ALERT.RxBufferOverflow</a><br>&nbsp;&nbsp;&nbsp;&nbsp;- <a href="../../../port-controller/registers/alert/#transmit-sop-message-successful">ALERT.TxMessageSuccessful</a><br>&nbsp;&nbsp;&nbsp;&nbsp;- <a href="../../../port-controller/registers/alert/#transmit-sop-message-discarded">ALERT.TxMessageDiscarded</a><br>&nbsp;&nbsp;&nbsp;&nbsp;- <a href="../../../port-controller/registers/alert/#transmit-sop-message-failed">ALERT.TxMessageFailed</a><br>- Set <a href="../../../port-controller/registers/receive-detect/#receive_detect">RECEIVE_DETECT</a> to a non-zero<br>&nbsp;&nbsp;value (enable TCPC receiver)" as pe_hard_reset_complete_entry
        }

        %% >>> Configure State Transitions <<< %%

        [*] --> reset_layer : A Cable Reset<small><sup><a class="footnote-ref" href="#hr#colon;fn#colon;1">1</a></sup></small> was received,<br><a href="../../../port-controller/registers/alert/#received-hard-reset">ALERT.HardReset</a> is asserted, or the<br> Policy Engine requested a Hard Reset

        reset_layer --> indicate_hard_reset : Protocol Layer reset complete and<br>reset initiated by Port Partner or Cable Plug
        reset_layer --> request_hard_reset : Protocol Layer reset complete and<br>reset initiated by Policy Engine

        indicate_hard_reset --> wait_for_pe_hard_reset_complete : Policy Engine informed

        request_hard_reset --> wait_for_phy_hard_reset_complete : PHY Hard Reset or Cable Reset<br>request sent

        wait_for_phy_hard_reset_complete --> phy_hard_reset_requested :<a href="../../../port-controller/registers/alert/#transmit-sop-message-failed">ALERT.TxMessageFailed</a> and<br><a href="../../../port-controller/registers/alert/#transmit-sop-message-successful">ALERT.TxMessageSuccessful</a>
        
        phy_hard_reset_requested --> wait_for_pe_hard_reset_complete : Policy Engine informed

        wait_for_pe_hard_reset_complete --> pe_hard_reset_complete : Policy Engine completed<br>Hard Reset

        pe_hard_reset_complete --> [*] : Physical Layer informed

        class reset_layer_entry,indicate_hard_reset_entry,request_hard_reset_entry,wait_for_phy_hard_reset_complete_entry,phy_hard_reset_requested_entry,wait_for_pe_hard_reset_complete_entry,pe_hard_reset_complete_entry onEntry
    ```
    { data-search-exclude }

    ***

    <div class="footnote">
      <ol>
          <li id="hr:fn:1">
            <p>A Cable Reset is detected when <a href="../../../port-controller/registers/alert/#received-sop-message-status">ALERT.RxStatus</a> is asserted and <a href="../../../port-controller/registers/receive-buffer/#received-sop-message">RX_BUF_FRAME_TYPE.RxMessage</a>=<code>110b</code></p>
          </li>
      </ol>
    </div>
