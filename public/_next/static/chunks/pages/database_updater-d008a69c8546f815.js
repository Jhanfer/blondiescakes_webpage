(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[722],{1947:function(e,t,a){(window.__NEXT_P=window.__NEXT_P||[]).push(["/database_updater",function(){return a(1436)}])},1436:function(e,t,a){"use strict";a.r(t),a.d(t,{Button_85ebc0a5e199090235dd4b060448888d:function(){return Button_85ebc0a5e199090235dd4b060448888d},Button_de432a9fae9001633054ecd39b1c5ae8:function(){return Button_de432a9fae9001633054ecd39b1c5ae8},Div_ac2a89ea84667d600a059f034bd91dfe:function(){return Div_ac2a89ea84667d600a059f034bd91dfe},Fragment_586cae509a4822c2f6f2544154f51844:function(){return Fragment_586cae509a4822c2f6f2544154f51844},Fragment_cf53a535ae2e610a113dd361eb6ac95b:function(){return Fragment_cf53a535ae2e610a113dd361eb6ac95b},Textfield__root_8333e743bf93caa32081d387cfcc0a83:function(){return Textfield__root_8333e743bf93caa32081d387cfcc0a83},Textfield__root_a17dd2219907fb60abadb4909ff629f9:function(){return Textfield__root_a17dd2219907fb60abadb4909ff629f9},Textfield__root_b4bdd9b7b7e6b2b02e5d9fe05bffb108:function(){return Textfield__root_b4bdd9b7b7e6b2b02e5d9fe05bffb108},Toaster_89416713a273995fc60191a4cf573054:function(){return Toaster_89416713a273995fc60191a4cf573054},default:function(){return Component}});var n=a(2729),r=a(6811),c=a(7294),i=a(687),o=a(6608),l=a(9894),d=a(917),f=a(4712),s=a(3954),u=a(5301),b=a(1664),p=a.n(b),_=a(9008),h=a.n(_);function _templateObject(){let e=(0,n._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _templateObject=function(){return e},e}function Toaster_89416713a273995fc60191a4cf573054(){let[e,t]=(0,c.useContext)(i.kc);o.xL.__toast=f.A;let[a,n]=(0,c.useContext)(i.DR),l={description:"Check if server is reachable at ".concat((0,o.LH)(s.Ks).href),closeButton:!0,duration:12e4,id:"websocket-error"},[d,u]=(0,c.useState)(!1);return(0,c.useEffect)(()=>{n.length>=2?d||f.A.error("Cannot connect to server: ".concat(n.length>0?n[n.length-1].message:"","."),{...l,onDismiss:()=>u(!0)}):(f.A.dismiss("websocket-error"),u(!1))},[n]),(0,r.tZ)(f.x,{closeButton:!1,expand:!0,position:"bottom-right",richColors:!0,theme:e})}function Button_85ebc0a5e199090235dd4b060448888d(){let[e,t]=(0,c.useContext)(i.DR),a=(0,c.useCallback)(t=>e([(0,o.ju)("state.backend_updater.reset_data",{})],t,{}),[e,o.ju]);return(0,r.tZ)(u.zx,{css:{fontFamily:"pertili","--default-font-family":"pertili",cursor:"pointer",variant:"solid",radius:"none",backgroundColor:"#F7E6DB",color:"#463626","&:hover":{backgroundColor:"#B6985E"}},onClick:a,size:"3",children:"cerrar"})}function Button_de432a9fae9001633054ecd39b1c5ae8(){let[e,t]=(0,c.useContext)(i.DR),a=(0,c.useCallback)(t=>e([(0,o.ju)("state.backend_updater.update_data",{})],t,{}),[e,o.ju]);return(0,r.tZ)(u.zx,{css:{fontFamily:"pertili","--default-font-family":"pertili",cursor:"pointer",variant:"solid",radius:"none",backgroundColor:"#F7E6DB",color:"#463626","&:hover":{backgroundColor:"#B6985E"}},onClick:a,children:"SUBIR"})}function Textfield__root_8333e743bf93caa32081d387cfcc0a83(){let[e,t]=(0,c.useContext)(i.DR),a=(0,c.useCallback)(t=>e([(0,o.ju)("state.backend_updater.set_image_url",{image_url:t.target.value})],t,{}),[e,o.ju]);return(0,r.tZ)(u.nv.f,{onBlur:a,placeholder:"url de imagen"})}function Textfield__root_a17dd2219907fb60abadb4909ff629f9(){let[e,t]=(0,c.useContext)(i.DR),a=(0,c.useCallback)(t=>e([(0,o.ju)("state.backend_updater.set_url_purchase",{url_purchase:t.target.value})],t,{}),[e,o.ju]);return(0,r.tZ)(u.nv.f,{onBlur:a,placeholder:"url de compra"})}function Div_ac2a89ea84667d600a059f034bd91dfe(){let[e,t]=(0,c.useContext)(i.DR);return(0,r.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},title:"Connection Error: ".concat(t.length>0?t[t.length-1].message:""),children:(0,r.tZ)(Fragment_cf53a535ae2e610a113dd361eb6ac95b,{})})}let m=(0,d.F4)(_templateObject());function Fragment_cf53a535ae2e610a113dd361eb6ac95b(){let[e,t]=(0,c.useContext)(i.DR);return(0,r.tZ)(c.Fragment,{children:(0,o.oA)(t.length>0)?(0,r.tZ)(c.Fragment,{children:(0,r.tZ)(l.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"33px",right:"33px",animation:"".concat(m," 1s infinite")},size:32})}):(0,r.tZ)(c.Fragment,{})})}function Textfield__root_b4bdd9b7b7e6b2b02e5d9fe05bffb108(){let[e,t]=(0,c.useContext)(i.DR),a=(0,c.useCallback)(t=>e([(0,o.ju)("state.backend_updater.set_title",{title:t.target.value})],t,{}),[e,o.ju]);return(0,r.tZ)(u.nv.f,{onBlur:a,placeholder:"titulo del art\xedculo"})}function Fragment_586cae509a4822c2f6f2544154f51844(){let e=(0,c.useContext)(i.M4.state__page_state);return(0,r.tZ)(c.Fragment,{children:(0,o.oA)(e.database_data)?(0,r.tZ)(c.Fragment,{children:(0,r.BX)(u.kC,{align:"center",className:"rx-Stack",css:{width:"100%",padding:"1em"},direction:"column",justify:"center",gap:"2",children:[(0,r.tZ)(u.xv,{as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal"},children:"NUESTROS PRODUCTOS"}),(0,r.tZ)(u.kC,{align:"center",className:"rx-Stack",direction:"row",gap:"3",children:(0,r.tZ)(u.kC,{align:"center",css:{width:"100%"},justify:"center",gap:"7",wrap:"wrap",children:e.database_data.map((e,t)=>(0,r.BX)(u.kC,{align:"center",className:"rx-Stack",direction:"column",justify:"center",gap:"5",children:[(0,r.tZ)(u.rU,{asChild:!0,css:{textDecoration:"None","&:hover":{color:"var(--accent-8)"},cursor:"pointer"},target:(0,o.oA)(!0)?"_blank":"",children:(0,r.tZ)(p(),{href:e.url_purchase,passHref:!0,children:(0,r.tZ)("img",{align:"center",alt:"producto: ".concat(e.title),css:{background:"#F7E6DB",width:"15em",height:"auto"},src:e.image_url})})}),(0,r.tZ)(u.xv,{align:"center",as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal",color:"#463626"},size:"3",children:e.title}),(0,r.tZ)(u.rU,{asChild:!0,css:{textDecoration:"None","&:hover":{color:"var(--accent-8)"},cursor:"pointer"},target:(0,o.oA)(!0)?"_blank":"",children:(0,r.tZ)(p(),{href:e.url_purchase,passHref:!0,children:(0,r.tZ)(u.zx,{css:{fontFamily:"pertili","--default-font-family":"pertili",cursor:"pointer",variant:"solid",radius:"none",backgroundColor:"#F7E6DB",color:"#463626","&:hover":{backgroundColor:"#B6985E"},width:"100%",justify:"center"},radius:"none",children:"PEDIR"})})})]},t))})})]})}):(0,r.tZ)(c.Fragment,{})})}function Component(){return(0,r.BX)(c.Fragment,{children:[(0,r.BX)(c.Fragment,{children:[(0,r.tZ)(Div_ac2a89ea84667d600a059f034bd91dfe,{}),(0,r.tZ)(Toaster_89416713a273995fc60191a4cf573054,{})]}),(0,r.BX)(u.kC,{align:"center",className:"rx-Stack",css:{paddingTop:"10em"},direction:"column",justify:"center",gap:"3",children:[(0,r.BX)(u.kC,{align:"center",className:"rx-Stack",css:{width:"90%",background:"grey",height:"5em",paddingLeft:"3em",paddingRight:"3em"},direction:"row",justify:"between",gap:"3",children:[(0,r.BX)(u.Vq.fC,{children:[(0,r.tZ)(u.Vq.xz,{children:(0,r.tZ)(u.zx,{css:{fontFamily:"pertili","--default-font-family":"pertili",cursor:"pointer",variant:"solid",radius:"none",backgroundColor:"#75D516",color:"#000000","&:hover":{backgroundColor:"#B6985E"}},children:"crear nuevo art\xedculo"})}),(0,r.BX)(u.Vq.VY,{children:[(0,r.tZ)(u.kC,{align:"center",className:"rx-Stack",css:{paddingBottom:"3em"},direction:"column",gap:"3",children:(0,r.tZ)(u.X6,{children:"Creaci\xf3n de art\xedculo"})}),(0,r.BX)(u.kC,{align:"start",className:"rx-Stack",css:{width:"100%",paddingBottom:"3em"},direction:"column",justify:"center",gap:"5",children:[(0,r.BX)(u.kC,{css:{width:"100%"},justify:"between",children:[(0,r.tZ)(u.xv,{as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal"},children:"T\xedtulo del art\xedculo"}),(0,r.tZ)(Textfield__root_b4bdd9b7b7e6b2b02e5d9fe05bffb108,{})]}),(0,r.BX)(u.kC,{css:{width:"100%"},justify:"between",children:[(0,r.tZ)(u.xv,{as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal"},children:"URL de la imagen(URL directa)"}),(0,r.tZ)(Textfield__root_8333e743bf93caa32081d387cfcc0a83,{})]}),(0,r.BX)(u.kC,{css:{width:"100%"},justify:"between",children:[(0,r.tZ)(u.xv,{as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal"},children:"URL de whatsapp"}),(0,r.tZ)(Textfield__root_a17dd2219907fb60abadb4909ff629f9,{})]}),(0,r.tZ)(Button_de432a9fae9001633054ecd39b1c5ae8,{})]}),(0,r.tZ)(u.kC,{align:"center",className:"rx-Stack",direction:"column",gap:"3",children:(0,r.tZ)(u.Vq.x8,{children:(0,r.tZ)(u.kC,{children:(0,r.tZ)(Button_85ebc0a5e199090235dd4b060448888d,{})})})})]})]}),(0,r.tZ)(u.zx,{css:{fontFamily:"pertili","--default-font-family":"pertili",cursor:"pointer",variant:"solid",radius:"none",backgroundColor:"#ec1c1c",color:"#000000","&:hover":{backgroundColor:"#B6985E"}},children:"eliminar art\xedculo"})]}),(0,r.tZ)(u.xv,{as:"p",css:{fontFamily:"pertili","--default-font-family":"pertili",whiteSpace:"normal"},children:"ITEMS DE LA TIENDA"}),(0,r.tZ)(u.kC,{gap:"8",wrap:"wrap",children:(0,r.tZ)(Fragment_586cae509a4822c2f6f2544154f51844,{})})]}),(0,r.BX)(h(),{children:[(0,r.tZ)("title",{children:"Database"}),(0,r.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}}},function(e){e.O(0,[477,664,774,888,179],function(){return e(e.s=1947)}),_N_E=e.O()}]);