(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[722],{1947:function(e,t,a){(window.__NEXT_P=window.__NEXT_P||[]).push(["/database_updater",function(){return a(1436)}])},1436:function(e,t,a){"use strict";a.r(t),a.d(t,{Button_0d5e52f0d7aa0166aa5dca5b91faee21:function(){return Button_0d5e52f0d7aa0166aa5dca5b91faee21},Button_2d9f057833f2ec53497b4161d729876b:function(){return Button_2d9f057833f2ec53497b4161d729876b},Button_85ebc0a5e199090235dd4b060448888d:function(){return Button_85ebc0a5e199090235dd4b060448888d},Div_ac2a89ea84667d600a059f034bd91dfe:function(){return Div_ac2a89ea84667d600a059f034bd91dfe},Flex_7e912b03b01c57c2461ce1452d9a1a27:function(){return Flex_7e912b03b01c57c2461ce1452d9a1a27},Fragment_cf53a535ae2e610a113dd361eb6ac95b:function(){return Fragment_cf53a535ae2e610a113dd361eb6ac95b},Fragment_e8891c48fdebb457b5be3a38495d73df:function(){return Fragment_e8891c48fdebb457b5be3a38495d73df},Textfield__root_8333e743bf93caa32081d387cfcc0a83:function(){return Textfield__root_8333e743bf93caa32081d387cfcc0a83},Textfield__root_a17dd2219907fb60abadb4909ff629f9:function(){return Textfield__root_a17dd2219907fb60abadb4909ff629f9},Textfield__root_b4bdd9b7b7e6b2b02e5d9fe05bffb108:function(){return Textfield__root_b4bdd9b7b7e6b2b02e5d9fe05bffb108},Toaster_89416713a273995fc60191a4cf573054:function(){return Toaster_89416713a273995fc60191a4cf573054},default:function(){return Component}});var n=a(2729),r=a(6811),c=a(7294),i=a(687),d=a(6608),o=a(9894),l=a(917),u=a(4712),f=a(3954),s=a(5301),b=a(9008),_=a.n(b);function _templateObject(){let e=(0,n._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _templateObject=function(){return e},e}function Textfield__root_a17dd2219907fb60abadb4909ff629f9(){let[e,t]=(0,c.useContext)(i.DR),a=(0,c.useCallback)(t=>e([(0,d.ju)("state.backend_updater.set_url_purchase",{url_purchase:t.target.value})],t,{}),[e,d.ju]);return(0,r.tZ)(s.nv.f,{onBlur:a,placeholder:"url de compra"})}let p=(0,l.F4)(_templateObject());function Button_85ebc0a5e199090235dd4b060448888d(){let[e,t]=(0,c.useContext)(i.DR),a=(0,c.useCallback)(t=>e([(0,d.ju)("state.backend_updater.reset_data",{})],t,{}),[e,d.ju]);return(0,r.tZ)(s.zx,{css:{fontFamily:"pertili","--default-font-family":"pertili",cursor:"pointer",variant:"solid",radius:"none",backgroundColor:"#F7E6DB",color:"#463626","&:hover":{backgroundColor:"#B6985E"}},onClick:a,size:"3",children:"cerrar"})}function Toaster_89416713a273995fc60191a4cf573054(){let[e,t]=(0,c.useContext)(i.kc);d.xL.__toast=u.A;let[a,n]=(0,c.useContext)(i.DR),o={description:"Check if server is reachable at ".concat((0,d.LH)(f.Ks).href),closeButton:!0,duration:12e4,id:"websocket-error"},[l,s]=(0,c.useState)(!1);return(0,c.useEffect)(()=>{n.length>=2?l||u.A.error("Cannot connect to server: ".concat(n.length>0?n[n.length-1].message:"","."),{...o,onDismiss:()=>s(!0)}):(u.A.dismiss("websocket-error"),s(!1))},[n]),(0,r.tZ)(u.x,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function Fragment_e8891c48fdebb457b5be3a38495d73df(){let e=(0,c.useContext)(i.M4.state__page_state),[t,a]=(0,c.useContext)(i.DR);return(0,r.tZ)(c.Fragment,{children:(0,d.oA)(e.database_data)?(0,r.tZ)(c.Fragment,{children:(0,r.tZ)(s.kC,{align:"center",className:"rx-Stack",css:{width:"100%",padding:"1em"},direction:"column",justify:"center",gap:"2",children:(0,r.tZ)(s.kC,{align:"center",className:"rx-Stack",direction:"row",gap:"3",children:(0,r.tZ)(s.kC,{align:"center",css:{width:"100%"},justify:"center",gap:"7",wrap:"wrap",children:e.database_data.map((e,a)=>(0,r.tZ)(s.kC,{align:"center",className:"rx-Stack",direction:"column",justify:"center",gap:"5",children:(0,r.BX)(s.Zb,{css:{align:"center",justify:"center"},children:[(0,r.tZ)(s.xv,{as:"label",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal"},size:"2",children:(0,r.BX)(s.kC,{gap:"2",children:[(0,r.tZ)(s.XZ,{onCheckedChange:a=>t([(0,d.ju)("state.backend_updater.select",{featured_id:e.id,checked:a})],a,{}),size:"2",value:e.id}),""]})}),(0,r.tZ)("img",{align:"center",alt:"producto: ".concat(e.title),css:{background:"#F7E6DB",width:"15em",height:"auto"},src:e.image_url}),(0,r.BX)(s.kC,{align:"start",className:"rx-Stack",direction:"column",gap:"4",children:[(0,r.tZ)(s.xv,{align:"center",as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal",color:"#463626"},size:"3",children:e.title}),(0,r.tZ)(s.xv,{align:"center",as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal",color:"#463626"},size:"3",children:e.image_url}),(0,r.tZ)(s.xv,{align:"center",as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal",color:"#463626"},size:"3",children:e.url_purchase}),(0,r.tZ)(s.xv,{align:"center",as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal",color:"#463626"},size:"3",children:"".concat(e.upload_time.slice(0,10)," ").concat(e.upload_time.slice(11,20))})]})]})},a))})})})}):(0,r.tZ)(c.Fragment,{})})}function Textfield__root_8333e743bf93caa32081d387cfcc0a83(){let[e,t]=(0,c.useContext)(i.DR),a=(0,c.useCallback)(t=>e([(0,d.ju)("state.backend_updater.set_image_url",{image_url:t.target.value})],t,{}),[e,d.ju]);return(0,r.tZ)(s.nv.f,{onBlur:a,placeholder:"url de imagen"})}function Button_0d5e52f0d7aa0166aa5dca5b91faee21(){let[e,t]=(0,c.useContext)(i.DR),a=(0,c.useCallback)(t=>e([(0,d.ju)("state.backend_updater.update_data",{}),(0,d.ju)("state.backend_updater.refresh_page",{})],t,{}),[e,d.ju]);return(0,r.tZ)(s.zx,{css:{fontFamily:"pertili","--default-font-family":"pertili",cursor:"pointer",variant:"solid",radius:"none",backgroundColor:"#F7E6DB",color:"#463626","&:hover":{backgroundColor:"#B6985E"}},onClick:a,children:"SUBIR"})}function Fragment_cf53a535ae2e610a113dd361eb6ac95b(){let[e,t]=(0,c.useContext)(i.DR);return(0,r.tZ)(c.Fragment,{children:(0,d.oA)(t.length>0)?(0,r.tZ)(c.Fragment,{children:(0,r.tZ)(o.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:"".concat(p," 1s infinite")},size:32})}):(0,r.tZ)(c.Fragment,{})})}function Div_ac2a89ea84667d600a059f034bd91dfe(){let[e,t]=(0,c.useContext)(i.DR);return(0,r.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: ".concat(t.length>0?t[t.length-1].message:""),children:(0,r.tZ)(Fragment_cf53a535ae2e610a113dd361eb6ac95b,{})})}function Flex_7e912b03b01c57c2461ce1452d9a1a27(){(0,c.useEffect)(()=>(e([(0,d.ju)("state.backend_updater.refresh_state_refresh",{})]),()=>{}),[]);let[e,t]=(0,c.useContext)(i.DR);return(0,r.BX)(s.kC,{align:"start",className:"rx-Stack",css:{width:"100%",paddingBottom:"3em"},direction:"column",justify:"center",gap:"5",children:[(0,r.BX)(s.kC,{css:{width:"100%"},justify:"between",children:[(0,r.tZ)(s.xv,{as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal"},children:"T\xedtulo del art\xedculo"}),(0,r.tZ)(Textfield__root_b4bdd9b7b7e6b2b02e5d9fe05bffb108,{})]}),(0,r.BX)(s.kC,{css:{width:"100%"},justify:"between",children:[(0,r.tZ)(s.xv,{as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal"},children:"URL de la imagen(URL directa)"}),(0,r.tZ)(Textfield__root_8333e743bf93caa32081d387cfcc0a83,{})]}),(0,r.BX)(s.kC,{css:{width:"100%"},justify:"between",children:[(0,r.tZ)(s.xv,{as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal"},children:"URL de whatsapp"}),(0,r.tZ)(Textfield__root_a17dd2219907fb60abadb4909ff629f9,{})]}),(0,r.tZ)(Button_0d5e52f0d7aa0166aa5dca5b91faee21,{})]})}function Textfield__root_b4bdd9b7b7e6b2b02e5d9fe05bffb108(){let[e,t]=(0,c.useContext)(i.DR),a=(0,c.useCallback)(t=>e([(0,d.ju)("state.backend_updater.set_title",{title:t.target.value})],t,{}),[e,d.ju]);return(0,r.tZ)(s.nv.f,{onBlur:a,placeholder:"titulo del art\xedculo"})}function Button_2d9f057833f2ec53497b4161d729876b(){let e=(0,c.useContext)(i.M4.state__backend_updater),[t,a]=(0,c.useContext)(i.DR),n=(0,c.useCallback)(e=>t([(0,d.ju)("state.backend_updater.delete_database_items",{}),(0,d.ju)("state.backend_updater.refresh_page",{})],e,{}),[t,d.ju]);return(0,r.tZ)(s.zx,{css:{fontFamily:"pertili","--default-font-family":"pertili",cursor:"pointer",variant:"solid",radius:"none",backgroundColor:"#ec1c1c",color:"#000000","&:hover":{backgroundColor:"#B6985E"}},disabled:e.checked,onClick:n,children:"eliminar art\xedculo"})}function Component(){return(0,r.BX)(c.Fragment,{children:[(0,r.BX)(c.Fragment,{children:[(0,r.tZ)(Div_ac2a89ea84667d600a059f034bd91dfe,{}),(0,r.tZ)(Toaster_89416713a273995fc60191a4cf573054,{})]}),(0,r.BX)(s.kC,{align:"center",className:"rx-Stack",css:{paddingTop:"10em"},direction:"column",justify:"center",gap:"3",children:[(0,r.BX)(s.kC,{align:"center",className:"rx-Stack",css:{width:"90%",background:"grey",height:"5em",paddingLeft:"3em",paddingRight:"3em"},direction:"row",justify:"between",gap:"3",children:[(0,r.BX)(s.Vq.fC,{children:[(0,r.tZ)(s.Vq.xz,{children:(0,r.tZ)(s.zx,{css:{fontFamily:"pertili","--default-font-family":"pertili",cursor:"pointer",variant:"solid",radius:"none",backgroundColor:"#75D516",color:"#000000","&:hover":{backgroundColor:"#B6985E"}},children:"crear nuevo art\xedculo"})}),(0,r.BX)(s.Vq.VY,{children:[(0,r.tZ)(s.kC,{align:"center",className:"rx-Stack",css:{paddingBottom:"3em"},direction:"column",gap:"3",children:(0,r.tZ)(s.X6,{children:"Creaci\xf3n de art\xedculo"})}),(0,r.tZ)(Flex_7e912b03b01c57c2461ce1452d9a1a27,{}),(0,r.tZ)(s.kC,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:(0,r.tZ)(s.Vq.x8,{children:(0,r.tZ)(s.kC,{children:(0,r.tZ)(Button_85ebc0a5e199090235dd4b060448888d,{})})})})]})]}),(0,r.tZ)(Button_2d9f057833f2ec53497b4161d729876b,{})]}),(0,r.tZ)(s.xv,{as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal"},children:"ITEMS DE LA TIENDA"}),(0,r.tZ)(s.kC,{gap:"8",wrap:"wrap",children:(0,r.tZ)(Fragment_e8891c48fdebb457b5be3a38495d73df,{})})]}),(0,r.BX)(_(),{children:[(0,r.tZ)("title",{children:"Database"}),(0,r.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}}},function(e){e.O(0,[477,774,888,179],function(){return e(e.s=1947)}),_N_E=e.O()}]);