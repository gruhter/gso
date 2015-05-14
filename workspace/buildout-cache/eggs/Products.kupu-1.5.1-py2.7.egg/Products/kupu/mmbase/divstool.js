var divids = 0;

/**
 * This tool is to create 'blocks'
 * $Id: divstool.js 205179 2008-09-19 15:55:36Z mihxil $
 */

function DivsTool() {
    /* tool to add 'divs' */

}
DivsTool.prototype = new KupuTool;

DivsTool.prototype.initialize = function(editor) {
    /* attach the event handlers */
    this.editor = editor;
    this.editor.logMessage(_("Div tool initialized"));
};

DivsTool.prototype.createDiv = function(divclass) {
    /* create a div */
    var currnode = this.editor.getSelectedNode();
    var currp = this.editor.getNearestParentOfType(currnode, 'p');

    var doc = this.editor.getInnerDocument();
    var div = doc.createElement('div');
    div.id = "createddiv_" + (divids++);
    if (divclass) {
        div.className = divclass;
    };
    var selection  = this.editor.getSelection();
    var fragment   = selection ? selection.cloneContents() : undefined;
    if(fragment == undefined || fragment.firstChild == undefined || fragment.firstChild.nodeType == Node.TEXT_NODE) {
        var child = doc.createElement("p");
        if (fragment != undefined) {
            child.appendChild(selection.cloneContents());
        }
        div.appendChild(child);
        if (child.childNodes.length == 0 || (child.childNodes.length == 1 && (child.firstChild.nodeValue == "" || child.firstChild.nodeValue == undefined))) {
            child.appendChild(doc.createTextNode("."));
        }
    } else {
        div.appendChild(fragment);
    }

    //var ser = new XMLSerializer();
    //alert("inserting " + ser.serializeToString(div));

    if (currp) {
        this.editor.logMessage(_("Found paragraph"));
        currp.parentNode.insertBefore(div, currp);
        this.editor.insertNodeAtSelection(doc.createTextNode(""), 1);
    } else {
        this.editor.logMessage(_("Didn't find paragraph"));
        //alert("Inserting " + div);
        div = this.editor.insertNodeAtSelection(div, 1);
    }

    this.editor.logMessage(_("Div inserted"));
    this.editor.updateState();
    return div;
};

DivsTool.prototype.setDivClass = function(divclass) {
    var currnode = this.editor.getSelectedNode();
    var currdiv = this.editor.getNearestParentOfType(currnode, 'div');
    if (currdiv) {
        currdiv.className = divclass;
    };
};

DivsTool.prototype.deleteDiv = function() {
    /* delete the current link */
    var currnode = this.editor.getSelectedNode();
    var linkel = this.editor.getNearestParentOfType(currnode, 'div');
    if (!linkel) {
        this.editor.logMessage(_('Not inside block'));
        return;
    };
    while (linkel.childNodes.length) {
        linkel.parentNode.insertBefore(linkel.childNodes[0], linkel);
    };
    linkel.parentNode.removeChild(linkel);

    this.editor.logMessage(_('Block removed'));
    this.editor.updateState();
};

DivsTool.prototype.createContextMenuElements = function(selNode, event) {
    /* create the 'Create link' or 'Remove link' menu elements */
    var ret = [];
    var link = this.editor.getNearestParentOfType(selNode, 'div');
    if (link) {
        ret.push(new ContextMenuElement(_('Delete block'), this.deleteDiv, this));
    }
    return ret;
};


function DivsToolBox(insertbuttonid, classselectid, toolboxid, plainclass, activeclass) {
    this.insertbutton = getFromSelector(insertbuttonid);
    this.classselect  = getFromSelector(classselectid);
    this.toolboxel    = getFromSelector(toolboxid);
    this.plainclass   = plainclass;
    this.activeclass  = activeclass;
    this.classRe = new RegExp('\\bfloat\\b', 'i');
}


DivsToolBox.prototype.initialize = function(tool, editor) {
    this.tool = tool;
    this.editor = editor;
    addEventHandler(this.classselect, "change", this.setDivClass, this);
    addEventHandler(this.insertbutton, "click", this.addDiv, this);
};

DivsToolBox.prototype.updateState = function(selNode, event) {
    /* update the state of the toolbox element */
    var divel = this.editor.getNearestParentOfType(selNode, 'div');
    if (divel && this.classRe.test(divel.className)) {
        // check first before setting a class for backward compatibility
        if (this.toolboxel) {
            this.toolboxel.className = this.activeclass;
            var divclass = divel.className ? divel.className : 'note';
            selectSelectItem(this.classselect, divclass);
        };
    } else {
        if (this.toolboxel) {
            this.toolboxel.className = this.plainclass;
        };
    };
};


DivsToolBox.prototype.addDiv = function() {
    /* add an div */
    var sel_class = this.classselect.options[this.classselect.selectedIndex].value;
    this.tool.createDiv(sel_class);
    this.editor.focusDocument();
};

DivsToolBox.prototype.setDivClass = function() {
    var sel_class = this.classselect.options[this.classselect.selectedIndex].value;
    this.tool.setDivClass(sel_class);
    this.editor.focusDocument();
};


